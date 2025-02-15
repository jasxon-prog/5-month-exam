from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny


class SalesmanListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Salesman.objects.all()
    serializer_class = serializers.SalesmanSerializer
    permission_classes = [AllowAny]  


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