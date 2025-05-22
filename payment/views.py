from django.shortcuts import redirect,HttpResponse,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings
from payment.models import Payment
from order.models import Order
from cart.models import Cart
@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        if razorpay_order_id and razorpay_payment_id and razorpay_signature:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            try:
                client.utility.verify_payment_signature({
                            'razorpay_order_id': razorpay_order_id,
                            'razorpay_payment_id': razorpay_payment_id,
                            'razorpay_signature': razorpay_signature
                })
            except razorpay.errors.SignatureVerificationError as e:
                print("Error in verifying ",e)
                redirect('show_cart')
            user = request.user
            payment = get_object_or_404(Payment,razorpay_order_id=razorpay_order_id)
            order = get_object_or_404(Order,order_uuid = payment.order.order_uuid)
            Cart.objects.filter(user=user).delete()
            payment.razorpay_payment_id  = razorpay_payment_id
            payment.payment_signature = razorpay_signature
            payment.amount = order.order_amount
            payment.status =  "COMPLETED"
            payment.method = "RAZORPAY"
            payment.user = user
            payment.save()
            order.payment_status = "Completed"
            import datetime
            order.pickup_date = datetime.datetime.now().date()
            order.status = 'Order placed' 
            order.save()
            return HttpResponse("successful payment")
        else:
            return redirect("show_cart")
    else:
        return redirect("show_cart")