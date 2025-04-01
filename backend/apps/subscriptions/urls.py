from django.urls import path
from .views import CreateCheckoutSession, StripeWebhookView

urlpatterns = [
    path('checkout/', CreateCheckoutSession.as_view()),
    path('webhook/', StripeWebhookView.as_view()),
]
