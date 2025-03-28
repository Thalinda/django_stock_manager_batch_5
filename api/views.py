
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer
from .models import Product,OrderItem,Order
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["GET","POST"]) #Decorator
def product_list(request):
    
    if request.method == "POST":
        serialize = ProductSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        products = Product.objects.all()
        serialize = ProductSerializer(products,many=True)
        return Response(serialize.data)

class GetProductListApiView(ListCreateAPIView):
       authentication_classes = [JWTAuthentication]
       permission_classes = [IsAuthenticated]
       serializer_class = ProductSerializer
       def get_queryset(self):
            print(self.request.user)
            return Product.objects.all()



class GetProductItemAPIView(RetrieveAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    
    
@api_view(['GET'])
def get_orders_products(request):
    ordered_products = OrderItem.objects.all()
    serializer = OrderItemSerializer(ordered_products,many=True)
    return Response(serializer.data)

    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    user_id = request.data.get("user")
    items_data = request.data.get("items",[])
    
    try:
        user = User.objects.get(id= user_id)
    except User.DoesNotExist:
        return Response({"error":"User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    order = Order.objects.create(user=user)
    
    for item in items_data:
        try:
            product = Product.objects.get(id =item["product_id"])
        except Product.DoesNotExist:
            return Response({"error":"No Items found"})
        
        quantity = item.get("quantity",1)
        OrderItem.objects.create(order=order,product=product,quantity=quantity)
        
    serialier = OrderSerializer(order)
    return Response(serialier.data,status=status.HTTP_201_CREATED)


# Nextweek 

# user authentication
# multiple validation
#  creating the app