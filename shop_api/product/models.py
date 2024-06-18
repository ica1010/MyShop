from django.db import models
from shortuuid.django_fields import ShortUUIDField
from category.models import Category
from userprofile.models import Vendor
# Create your models here.

class Product(models.Model):
    pid = ShortUUIDField(length=16, max_length=40,prefix="Prod-",alphabet="abcdefg1234",primary_key=True,)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=50, default='untitle product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.FileField(upload_to='media/Product_image', default='product.jgp')
    descriptions = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    price = models.IntegerField()
    promo_price = models.IntegerField(blank=True, null=True)

    add = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image = models.FileField(upload_to="media/Product_image",max_length=100, default='product.jgp')

    def __str__(self):
        return self.product.title
    
