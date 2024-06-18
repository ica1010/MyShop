from django.shortcuts import render
from . serializers import CategorySerializer
from . models import Category
from django.http import JsonResponse
from rest_framework import generics, mixins

from rest_framework.decorators import api_view

# @api_view(['GET'])
# def CategoryList(request):
#     category = Category.objects.all()
#     serializer = CategorySerializer(category, many = True )
#     return JsonResponse(serializer.data, safe=False)


class Category(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
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
