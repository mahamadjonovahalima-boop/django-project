from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Mea:
        model = Product
        fields = '__all__'