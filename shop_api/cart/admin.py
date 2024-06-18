from django.contrib import admin
from . models import *
# Register your models here.
class CartItemAdmin(admin.TabularInline):
    list_display = ['product','quantity','update','add']
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines=[CartItemAdmin]
    list_display = ['cid','user','add']
    list_filter = ('add','update','user')




admin.site.register(Cart,CartAdmin)
