from django.contrib import admin
from . models import *
# Register your models here.
class AddressAdmin(admin.TabularInline):
    list_display = ['vendor','consumer','address','phone','default','verified']
    model = Address

class UserAdmin(admin.ModelAdmin):
    
    list_display = ['uid','email','username']
    search_fields = ('username',)


class VendorAdmin(admin.ModelAdmin):
    inlines = [AddressAdmin]
    # inlines=[AddressAdmin]
    list_display = ['user','image','verified']
    list_filter = ('add',)
    search_fields = ('user',)

class ConsumerAdmin(admin.ModelAdmin):
    inlines=[AddressAdmin]
    list_display = ['user','image']
    list_filter = ('add',)
    search_fields = ('user',)


admin.site.register(User,UserAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Consumer,ConsumerAdmin)
# admin.site.register(Address,AddressAdmin)
