from django.shortcuts import render, redirect

from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    return render(request,'inventory/create_product.html' )