from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
import stripe
from apps.users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = stripe.checkout.Session.create(
            customer=request.user.stripe_customer_id,
            payment_method_types=['card'],
            line_items=[{'price': 'price_xxxxxx', 'quantity': 1}],  # <-- Configurar o price ID real
            mode='subscription',
            success_url='http://localhost:3000/dashboard',
            cancel_url='http://localhost:3000',
        )
        return Response({'url': session.url})

class StripeWebhookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.body
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except stripe.error.SignatureVerificationError:
            return Response(status=400)

        if event['type'] == 'customer.subscription.updated':
            subscription = event['data']['object']
            user = User.objects.get(stripe_customer_id=subscription['customer'])
            user.subscription_status = subscription['status']
            user.save()

        return Response({'status': 'success'})
