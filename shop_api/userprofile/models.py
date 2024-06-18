from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.


class User(AbstractUser):
    uid = ShortUUIDField(unique=True, length=4, max_length= 20 ,prefix='user-', alphabet='1234567890',editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60)
    #phone = PhoneNumberField()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Vendor(models.Model):
    image = models.FileField(upload_to='media/profile', default="./default_Profile.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)

    add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Consumer(models.Model):
    image = models.FileField(upload_to='media/profile', default="./default_Profile.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    

class Address(models.Model):
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE, related_name='consumer', blank=True , null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE, related_name='vendor', blank=True,null=True)
    address = models.CharField(max_length=500, default='not set')
    phone = models.PositiveIntegerField()
    verified = models.BooleanField(default=False)
    default = models.BooleanField(default=False)

    if vendor : 
        def __str__(self):
            return self.vendor.user.username
    else:
        def __str__(self):
            return self.consumer.user.username
    
User.groups.field.remote_field.related_name = 'user_groups'
User.user_permissions.field.remote_field.related_name = 'user_permissions'
Group.user_set.field.remote_field.related_name = 'group_users'
Permission.user_set.field.remote_field.related_name = 'permission_users'