from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Favorite, FavoriteItem
from . serializer import FavoriteSerializer,FavoriteItemSerializer
from django.http import JsonResponse
from rest_framework import generics, mixins




# @api_view(['GET'])
# def FavoriteList(request):
#     favorite = Favorite.objects.all()
#     serializer = FavoriteSerializer(favorite , many= True)
#     return JsonResponse({'favorites': serializer.data})

@api_view(['GET'])
def FavoriteItemList(request, fid):
    favoriteItem = FavoriteItem.objects.filter(favorite = fid) 
    serializer = FavoriteItemSerializer(favoriteItem, many=True)
    return JsonResponse({'favorite items': serializer.data})


class Favorite(generics.GenericAPIView, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
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
