from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ShippingRequestViewSet

router = DefaultRouter()
router.register("shippingrequest", ShippingRequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
