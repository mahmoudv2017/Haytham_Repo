from my_app import models
from rest_framework import serializers


class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.products
        fields = "__all__"