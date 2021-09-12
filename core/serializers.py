import re
from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework_simplejwt.token import RefrechToken

class ProductListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')



class UserSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', '_id' ,'username', 'name' ,'email')

    
    def get_name(self, obj):
        name = obj.first_name
        if name =='':
            name = obj.email
        return 
    
    def get__id(self, obj):
        return obj.id
