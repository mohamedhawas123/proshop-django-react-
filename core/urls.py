
from django.contrib import admin
from django.urls import path
from .views import  ProductList, ProductDetail, getUsers, getOrderById ,registerUser, addOrderItem
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)
from .views import MyTokenObtainPairView, getUserProfile, updateUserProfile



urlpatterns = [
    # path('', get_products, name="products" ),
    # path('<pk>', get_product, name="product" )
    path('api/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("users/profile", getUserProfile, name="profile"),
    path("users/updateProfile", updateUserProfile, name="update_profile"),
    path('users', getUsers, name="get_users"),
    path("users/register", registerUser, name="register"),
    path("",ProductList.as_view(), name="productList" ),
    path("<pk>/",ProductDetail.as_view(), name="detail" ),
    path("add/order/", addOrderItem, name="add_order"),
    path("getorder/<pk>", getOrderById, name="getOrderById")
]


