from rest_framework import serializers
from . models import Product, ProductImages

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['pid', 'vendor', 'title', 'category','image','descriptions','stock','price','promo_price','add','update'] 
        model = Product
        lookup_field = 'pid'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['product', 'image'] 
