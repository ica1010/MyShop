from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class Category(models.Model):
    cid = ShortUUIDField(length=16, max_length=40, prefix="Cat-", alphabet="abcdefg1234", primary_key=True, editable=False)
    title = models.CharField(max_length=50, default='untitle category')
    image = models.FileField(upload_to='media/category_image', default='category.jgp')

    add = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
