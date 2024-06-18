from rest_framework import serializers
from . models import Cart , CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cid', 'user', 'add', 'update'] 

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'add', 'update'] 
