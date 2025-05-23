from django.shortcuts import render

from rest_framework import viewsets , permissions , authentication
from products.models import Product
from . serializers import ProductSerializer
from products.permissions import IsStaffEditorPermission

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [ permissions.IsAdminUser , IsStaffEditorPermission]
