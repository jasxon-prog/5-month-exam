from rest_framework import serializers
from . import models


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductImage
        fields = ('images')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ("name", "image", "parent")

class SalesmanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Salesman
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'