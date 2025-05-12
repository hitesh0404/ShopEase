from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from .forms import LoginForm,RegisterForm
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required

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
    next = None
    def get(self,request):
        LoginView.next = request.GET.get("next")
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
                if LoginView.next:
                    var = LoginView.next
                    LoginView.next=None
                    return redirect(var)
                return redirect('/')
            else:
                return render(request,'account/login.html',{'form':form})
        else:
            return render(request,'account/login.html',{'form':form})
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'account/profile.html',context=context)