from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product',blank=True,null=True)
    
    @property
    def in_stock(self):
        return self.stock >0
    
    def __str__(self):
        return self.name
    
    

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING"
        CONFIRM = "CONFIRM"
        CANCELEd = "CANCELED"
    
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=StatusChoices.choices,default=StatusChoices.PENDING)
    product = models.ManyToManyField(Product,through="orderItem",related_name="orders")
    
    def __str__(self):
        return f"Self {self.order_id} {self.user.first_name}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    
    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"