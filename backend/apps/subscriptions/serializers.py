# Opcional caso precise expor dados de assinatura no frontend
from rest_framework import serializers

class SubscriptionSerializer(serializers.Serializer):
    status = serializers.CharField()
    stripe_customer_id = serializers.CharField()
