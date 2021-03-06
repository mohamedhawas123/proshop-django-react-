import re
from django.db.models import fields
from rest_framework import serializers
from .models import Product, ShippingAddress, OrderItem, Order
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ProductListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')



class UserSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    _id = serializers.SerializerMethodField()
    isAdmin = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', '_id' ,'username', 'name' ,'email', 'isAdmin')

    
    def get_name(self, obj):
        name = obj.first_name
        if name =='':
            name = obj.email
        return name

    def get_isAdmin(self, obj):
        return obj.is_staff
    
    def get__id(self, obj):
        return obj.id


class UserSerializerWithToken(UserSerializers):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', '_id' ,'username', 'name' ,'email', 'isAdmin', 'token')

    

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ('__all__')



class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    shippingAddress= serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('__all__')

    
    def get_orders(self, obj):
        items = obj.orderItem.all()
        return OrderItemSerializer(items, many=True).data
    
    def get_shippingAddress(self, obj):
        return ShippingAddressSerializer(obj.shippingAddress).data
    

    def get_user(self, obj):
        return UserSerializers(obj.user).data