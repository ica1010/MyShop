from django.urls import path, include
from . import views
from .views import ProductCrud
urlpatterns = [
    path('', views.ProductCrud.as_view(), name = 'products'),
    path('create/', ProductCrud.as_view(),name = 'create'),
    path('<pid>/', views.ProductCrud.as_view(), name = 'detail'),
    path('update/<pid>/', views.ProductCrud.as_view(),name = 'update'),
    path('delete/<pid>/', views.ProductCrud.as_view(), name = 'delete')
]
