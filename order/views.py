from django.shortcuts import render,redirect,get_object_or_404
from cart.models import Cart
# Create your views here.
import razorpay
from django.conf import settings
from .models import Order,OrderDetails
from uuid import uuid4
from account.models import Address
from datetime import datetime
from account.models import CustomerProfile
def checkout(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    user = request.user
    user = get_object_or_404(CustomerProfile, user = user)
    address = Address.objects.filter(customer=user)
    if len(address)==0:
        return redirect('add_address')
    order,create = Order.objects.get_or_create(
        customer=user,
        payment_status="Pending",
        defaults={
            "order_uuid" : uuid4(),
            "Shipping_address" : address[0],
            "customer" : user,
            "delivery_charge" : 10,
            "order_amount":0,
            "payment_status":"Pending",
            "pickup_date":datetime.now().date(),
            "delivery_date":datetime.now().date(),
        }
    )
    order.pickup_date = datetime.now().date()
    total=0
    cart = Cart.objects.filter(user=request.user)
    for cart_item in cart:
        value = cart_item.product.price * cart_item.quantity
        total+=value
        order_detail,create = OrderDetails.objects.get_or_create(
            order = order,
            product = cart_item.product,
            defaults={
                "quantity" : cart_item.quantity,
            }
        )
        order_detail.quantity = cart_item.quantity
        order_detail.save() 

    data = { "amount": int((total+order.delivery_charge)*100), "currency": "INR", "receipt": str(order.order_uuid) }
    payment = client.order.create(data=data)
    order.order_amount = total+order.delivery_charge
    context ={
        "data":data,
        "payment":payment,
        "order":order,
        "RAZORPAY_KEY_ID":settings.RAZORPAY_KEY_ID
    } 
    from payment.models import Payment
    my_payment,create = Payment.objects.get_or_create(
        order = order,
        defaults={
            'user': request.user,
            'razorpay_order_id': payment.get('id'),
            'amount' : order.order_amount,
            'status':"PENDING",
            'method': "RAZORPAY",
        }
    )
    my_payment.razorpay_order_id = payment.get('id')
    my_payment.amount =  order.order_amount
    my_payment.user = request.user
    my_payment.save()
    order.save()
    return render(request,'order/checkout.html',context)