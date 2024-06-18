from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Cart, CartItem
from . serialiazer import CartSerializer,CartItemSerializer
from django.http import JsonResponse
from rest_framework import generics, mixins



# @api_view(['GET'])
# def CartList(request):
#     cart = Cart.objects.all()
#     serializer = CartSerializer(cart , many= True)
#     return JsonResponse(serializer.data, safe=False)

# @api_view(['GET'])
# def CartItemList(request, cid):
#     cartItem = CartItem.objects.filter(cart = cid) 
#     serializer = CartItemSerializer(cartItem, many=True)
#     return JsonResponse({'cart items': serializer.data})


class Cart(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
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


class CartItem(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    lookup_field = 'pk'
    queryset = CartItem.objects.all()
    
    serializer_class = CartSerializer
    
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
