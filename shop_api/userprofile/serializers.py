from rest_framework import serializers
from . models import User ,Vendor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'email', 'username'] 

class VendorSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source='user', read_only = True)
    class Meta:
        model = Vendor
        fields = ['id','image','user', 'vendor', 'bio','verified', 'add']