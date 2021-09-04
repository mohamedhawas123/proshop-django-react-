from django.shortcuts import render
from .products import products
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_products(request): 
    return Response(products)



@api_view(['GET'])
def get_product(request, pk):
   product = next((x for x in products if x['_id']==pk ) ,None)
   return Response(product)

