from django.urls import path
from . import views



urlpatterns = [
    path("",views.product_list),
    path("<int:pk>",views.product),
    path("orders",views.get_orders),
    path("order-products",views.get_orders_products),
    path("create-order",views.create_order),
    
    
]

# 8000
# python maange.py runsever 192.168.1.1:8000