from django.contrib import admin
from . models import *
# Register your models here.
class ProductImagesAdmin(admin.TabularInline):
    list_display = ['image','product','update','add']
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImagesAdmin]
    list_display = ['pid','vendor','title','category','stock','price','promo_price']
    list_filter = ('add','update','vendor')
    search_fields = ('vendor', 'title')
    save_as = True


admin.site.register(Product,ProductAdmin)
