from re import L
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers
from .products import products
from django.http import JsonResponse, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProductListSerializers, UserSerializers, UserSerializerWithToken
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


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
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user 
    serializers = UserSerializers(user, many=False)
    return Response(serializers.data)


@api_view(['POST'])
def registerUser(request):
    data = request.data 
    print(request)
    try:

        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password =  make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message= {'detail': 'user is already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)



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

