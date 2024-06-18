from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userprofile.models import User
from product.models import Product
# Create your models here.


class Cart(models.Model):
    cid = ShortUUIDField(length=16, max_length=40,prefix="Cart-",alphabet="abcdefg1234",primary_key=True,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    add = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    add = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cart.user.username
