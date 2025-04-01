from django.urls import path
from .views import UserDashboardView, AdminDashboardView

urlpatterns = [
    path('user/', UserDashboardView.as_view()),
    path('admin/', AdminDashboardView.as_view()),
]
