from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.db.models import Sum


class SalesmanListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Salesman.objects.all()
    serializer_class = serializers.SalesmanSerializer
    permission_classes = [AllowAny]  

    data = models.Salesman.objects.aggregate(total=Sum('total_sell_product'))['total'] or 0


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [AllowAny]


class ProductImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer