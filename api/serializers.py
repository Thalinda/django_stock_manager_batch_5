from rest_framework import serializers
from .models import Order, Product,OrderItem




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock'
        )
        
        def validate_price(self,value):

            if value <=0:
                raise serializers.ValidationError(
                    "Price must be greater than 0"
                )
            return value
        

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many =False,read_only = True)
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
        )
 
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only = True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    
    class Meta:
        model = Order
        fields = (
            'order_id',
            'created_at',
            "user",
            "status",
            "items",
            "total_price",
        )