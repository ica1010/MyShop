from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer ,VendorSerializer
from .models import User,Vendor
from rest_framework import generics, mixins
from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def UserList(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user, many = True)
#     return JsonResponse({'Users' : serializer.data}, safe=False)

# @api_view(['GET'])
# def VendorList(request):
#     vendor = Vendor.objects.all()
#     serializer = VendorSerializer(vendor, many = True)
#     return JsonResponse(serializer.data, safe=False)


class User(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class Vendors(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
