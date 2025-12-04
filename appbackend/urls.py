from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('users/<id>/', views.Users.as_view(), name='users'),
    path('users/', views.Users.as_view(), name='users'),
    path('categories/', views.Categories.as_view(), name='category'),
    path('products/', views.Products.as_view(), name='product'),
    path('products/<id>/', views.Products.as_view(), name='product'),
]
