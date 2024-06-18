from django.contrib import admin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cid','image','title']
    list_filter = ['add','update']
    search_fields = ['title']
    save_as = True


admin.site.register(Category,CategoryAdmin)
