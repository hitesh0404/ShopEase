from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import redirect
                
from .forms import LoginForm,RegisterForm
from django.shortcuts import render,redirect
from django.views import View
# Create your views here.

def my_logout(request):
    logout(request)
    return redirect('login')

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'account/register.html',{'form':form})
    def post(self,request):
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'account/register.html',{'form':form})
    


    
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'account/login.html',{'form':form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'account/login.html',{'form':form})
        else:
            return render(request,'account/login.html',{'form':form})