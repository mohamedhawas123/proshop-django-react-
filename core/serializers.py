from rest_framework import serializers
from .models import Product

class ProductListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')