from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
import stripe
from django.conf import settings

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        stripe_customer = stripe.Customer.create(email=user.email)
        user.stripe_customer_id = stripe_customer['id']
        user.save()
        return Response(UserSerializer(user).data)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
