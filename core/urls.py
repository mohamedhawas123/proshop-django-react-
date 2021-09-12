
from django.contrib import admin
from django.urls import path
from .views import  ProductList, ProductDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)
from .views import MyTokenObtainPairView



urlpatterns = [
    # path('', get_products, name="products" ),
    # path('<pk>', get_product, name="product" )
    path('api/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("",ProductList.as_view(), name="productList" ),
    path("<pk>/",ProductDetail.as_view(), name="detail" )
]


