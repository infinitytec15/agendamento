from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.users.models import User
from apps.schedules.models import Appointment
from apps.clients.models import Client
import stripe
from django.utils import timezone
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "pending": Appointment.objects.filter(schedule__user=user, status="pending").count(),
            "done": Appointment.objects.filter(schedule__user=user, status="done").count(),
            "today": Appointment.objects.filter(schedule__user=user, date=timezone.now().date()).count(),
            "total_clients": Client.objects.filter(user=user).count()
        }
        return Response(data)

class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            "total_users": User.objects.count(),
            "active_users": User.objects.filter(is_active=True).count(),
            "subscribers": User.objects.exclude(subscription_status="canceled").count(),
            "total_appointments": Appointment.objects.count(),
            "total_revenue": stripe.Balance.retrieve()["available"][0]["amount"] / 100 if stripe.Balance.retrieve()["available"] else 0
        }
        return Response(data)
