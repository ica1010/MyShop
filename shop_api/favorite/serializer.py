from rest_framework import serializers
from . models import Favorite , FavoriteItem

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['fid', 'user', 'add', 'update'] 

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['favorite', 'product','add'] 
