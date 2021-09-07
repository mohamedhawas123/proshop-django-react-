
from django.contrib import admin
from django.urls import path
from .views import  ProductList, ProductDetail

urlpatterns = [
    # path('', get_products, name="products" ),
    # path('<pk>', get_product, name="product" )
    path("",ProductList.as_view(), name="productList" ),
    path("<pk>/",ProductDetail.as_view(), name="detail" )
]


