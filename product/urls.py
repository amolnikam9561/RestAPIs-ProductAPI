# from django.contrib import admin
from django.urls import path,include
from .views import product_create, product_list,product_detail,delete_product,update_product

urlpatterns = [
    path('products/',product_list, name='product_list'),
    path('products/create/',product_create, name='product_create'),
    path('products/<int:pk>/',product_detail, name='product_detail'),
    path('products/update/<int:id>/',update_product, name='update_product'),
    path('products/delete/<int:id>/',delete_product, name='delete_product'),
    
     
]
