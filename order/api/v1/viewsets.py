from rest_framework import authentication
from order.models import ShippingRequest
from .serializers import ShippingRequestSerializer
from rest_framework import viewsets


class ShippingRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingRequestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ShippingRequest.objects.all()
