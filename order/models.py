from django.db import models
from account.models import CustomerProfile
# Create your models here.

status_choices = [
    ('Order placed'      ,   'Order placed'),
    ('Order Confirmed'   ,   'Order Confirmed'),
    ('Order processing'  ,   'Order processing'),
    ('Dispatched'        ,   'Dispatched'),
    ('In Transit'        ,   'In Transit'),
    ('Out for delivery'  ,   'Out for delivery'),
    ('Delivered'         ,   'Delivered'),
    ('cancelled'         ,   'cancelled'),
    ('pending'           ,   'pending'),
    ('Completed'         ,   'Completed'),
    ('refunded'          ,   'refunded'),
]
payment_status_choices = [
    ('Pending' ,  'Pending'),
    ('Completed'  ,   'Completed'),
    ('Rejected'  ,   'Rejected'),
    ('Processing'  ,   'Processing'),
]

from account.models import Address
class Order(models.Model):
    order_uuid = models.UUIDField(primary_key=True,max_length=128)
    Shipping_address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(CustomerProfile,on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=30,choices=status_choices)
    delivery_charge = models.DecimalField(max_digits=10,decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)
    order_amount = models.DecimalField(max_digits=12,decimal_places=2)
    payment_status = models.CharField(max_length=20,choices=payment_status_choices)
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    @property
    def order_value(self):
        return self.order_amount + self.delivery_charge


from inventory.models import Product
class OrderDetails(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    @property
    def total_amount(self):
        return self.product.price * self.quantity

