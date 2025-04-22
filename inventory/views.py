from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    return render(request,'inventory/create_product.html' )

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'inventory/product_detail.html',{'product':product})

def product_delete(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == "GET":
        return render(request,'inventory/delete_confirmation.html',{'product':product})
    elif request.method == "POST":
        product.delete()
    return redirect('product_list')