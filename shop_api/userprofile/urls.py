from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.User.as_view()),
    path('vendor/',views.Vendors.as_view())
]
