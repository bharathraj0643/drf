from django.shortcuts import render

from rest_framework import viewsets
from products.models import Product
from .serializers import ProductSerializer

from . mixins import StaffEditorPermissionMixin

class ProductViewset(StaffEditorPermissionMixin,viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer