from re import L
from django.shortcuts import render
from .products import products
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product

# @api_view(['GET'])
# def get_products(request): 
#     return Response(products)


# @api_view(['GET'])
# def get_product(request, pk):
#    product = next((x for x in products if x['_id']==pk ) ,None)
#    return Response(product)


class ProductList(ListAPIView):
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()



class ProductDetail(RetrieveAPIView):
    serializer_class  = ProductListSerializers
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    