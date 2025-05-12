from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from inventory.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    context = {
        'cart':cart
    }
    return render(request,'cart/cart.html',context)

@login_required
def add_to_cart(request,id):
    user = request.user
    product = get_object_or_404(Product,id=id)
    cart , create = Cart.objects.update_or_create(user=user,product = product)
    if create:
        cart.quantity = 1
    else:
        cart.quantity += 1
        cart.save()
    return redirect("show_cart")


@login_required
def increase_quantity(request,id):
    cart = get_object_or_404(Cart,id=id)
    cart.quantity +=1
    cart.save()
    return redirect('show_cart')

@login_required
def decrease_quantity(request,id):
    cart = get_object_or_404(Cart,id=id)
    if cart.quantity>1:
        cart.quantity -=1
        cart.save()
    else:
        cart.delete() 
    return redirect('show_cart')
