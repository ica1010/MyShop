from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . views import homePage
urlpatterns = [
    path('', homePage ),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('category/', include('category.urls')),
    path('favorite/', include('favorite.urls')),
    path('user/', include('userprofile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)