
from django.contrib import admin
from django.urls import path
from .views import get_products, get_product

urlpatterns = [
    path('', get_products, name="products" ),
    path('<pk>', get_product, name="product" )
]


