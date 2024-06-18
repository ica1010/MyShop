from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userprofile.models import User
from product.models import Product
# Create your models here.


class Favorite(models.Model):
    fid = ShortUUIDField(length=16, max_length=40,prefix="Fav-",alphabet="abcdefg1234",primary_key=True,)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    add = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.favorite.user.username
