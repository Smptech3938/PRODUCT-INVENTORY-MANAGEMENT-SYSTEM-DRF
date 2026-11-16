from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields="__all__"
        read_only_fields=['created_at','id']
        