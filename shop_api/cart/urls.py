from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Cart.as_view()),
    path('<id>', views.CartItem.as_view())
]
