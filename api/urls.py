from django.urls import path
from . import views



urlpatterns = [
    path("",views.GetProductListApiView.as_view()),
    path("<int:pk>",views.GetProductItemAPIView.as_view()),
    path("orders",views.get_orders),
    path("order-products",views.get_orders_products),
    path("create-order",views.create_order),
    
    
]

# 8000
# python maange.py runsever 192.168.1.1:8000