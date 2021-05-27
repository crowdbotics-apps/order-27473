from django.conf import settings
from django.db import models


class ShippingRequest(models.Model):
    "Generated Model"
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()


# Create your models here.
