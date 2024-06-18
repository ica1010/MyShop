from django.contrib import admin
from . models import *
# Register your models here.
class FavoriteItemAdmin(admin.TabularInline):
    list_display = ['product','update','add']
    model = FavoriteItem

class FavoriteAdmin(admin.ModelAdmin):
    inlines=[FavoriteItemAdmin]
    list_display = ['fid','user','add']
    list_filter = ('add','user')




admin.site.register(Favorite,FavoriteAdmin)
