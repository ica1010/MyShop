from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class Category(models.Model):
    cid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="Cat-",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    title = models.CharField(max_length=50, default='untitle category')
    image = models.ImageField(upload_to='category_image')

    def __str__(self):
        return self.title

class Product(models.Model):
    pid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="Prod-",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    title = models.CharField(max_length=50, default='untitle product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='Product_image')
    descriptions = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
