from django.db import models
from account.models import User
from inventory.models import Product
from django.forms import ValidationError

# Create your models here.
def quantity_validator(value):
    if value<1:
        raise ValidationError(f'{value} is less then 1')

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[quantity_validator],default=1)
    added_on = models.DateTimeField(auto_now_add=True)  #executes only onces
    updated_on = models.DateTimeField(auto_now=True)    #executes every time
    def __str__(self):
        return f'{self.user.username} added {self.product.name}'
    class Meta:
        unique_together = ['user','product']
        db_table = 'cart'
        ordering = ['-quantity']