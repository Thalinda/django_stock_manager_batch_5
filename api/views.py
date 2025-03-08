
from api.serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serialize = ProductSerializer(products,many=True)
    
    return Response(serialize.data)


@api_view(['GET'])
def product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product)
    return Response(
        serializer.data
    )