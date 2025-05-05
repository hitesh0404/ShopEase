from django.shortcuts import render
from .models import Carousel
# Create your views here.
def home(request):
    carousel = Carousel.objects.all()
    return render(request,'index.html',{'carousel':carousel})