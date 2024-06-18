from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Category.as_view()),
    path('create/', views.Category.as_view()),
    path('<pk>/', views.Category.as_view()),
    path('update/<pk>/', views.Category.as_view()),
    path('delete/<pk>/', views.Category.as_view())
]
