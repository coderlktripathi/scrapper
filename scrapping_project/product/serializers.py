from rest_framework import serializers
from product.models import Product 

# Lead Serializer
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product 
    fields = '__all__'
