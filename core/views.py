from re import L
from django.shortcuts import render
from rest_framework import serializers
from .products import products
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializers, UserSerializers, UserSerializerWithToken
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    

    #     return token
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        # data['username'] = self.user.username
        # data['email'] = self.user.email

        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value

        
    

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class ProductList(ListAPIView):
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()


@api_view(['GET'])
def getUserProfile(request):
    user = request.user 
    serializers = UserSerializers(user, many=False)
    return Response(serializers.data)


class ProductDetail(RetrieveAPIView):
    serializer_class  = ProductListSerializers
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    



# @api_view(['GET'])
# def get_products(request): 
#     return Response(products)


# @api_view(['GET'])
# def get_product(request, pk):
#    product = next((x for x in products if x['_id']==pk ) ,None)
#    return Response(product)

