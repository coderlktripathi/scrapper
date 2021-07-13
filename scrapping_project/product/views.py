from django.shortcuts import render

from product.models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
