from rest_framework import serializers
from . models import Category
class CategorySerializer(serializers.ModelSerializer):
    # product = serializers.CharField(source='category', read_only = True)
    class Meta:
        model = Category 
        fields = ['cid','title','image','add','update'] 