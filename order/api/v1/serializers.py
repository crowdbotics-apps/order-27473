from rest_framework import serializers
from order.models import ShippingRequest


class ShippingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRequest
        fields = "__all__"
