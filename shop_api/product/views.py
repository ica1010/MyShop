from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Product
from .serialisers import ProductSerializer

# Create your views here.

class ProductCrud(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pid'
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
         instance.delete()
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pid') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        if kwargs.get('pid') is not None:
            return self.update(request, *args, **kwargs)
        else:
            pass
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Note: Remember to handle permissions and authentication as needed.
 