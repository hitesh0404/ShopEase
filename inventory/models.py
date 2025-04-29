from django.db import models
from account.models import SupplierProfile


class Brand(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='brand_logo')
    est_date = models.DateField()
    tagline = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):
    category = models.ManyToManyField(Category)
    suplier = models.ForeignKey(SupplierProfile,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product_images/main')
    price = models.DecimalField(max_digits=12,decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now_add=True,null=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='product_images')