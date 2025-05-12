from django.shortcuts import render
from cart.models import Cart
# Create your views here.


def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    total=0
    for i in cart:
        total += i.product.price * i.product.quantity
    return render(request,'order/checkout.html',{'total':total})
