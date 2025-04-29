from django.shortcuts import render
from django.views import View
# Create your views here.
from .forms import LoginForm
class RegisterView(View):
    pass
class LoginView(View):
    
    def get(self,request):
        form = LoginForm()
        return render(request,'account/login.html',{'form':form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            from django.contrib.auth import authenticate
            user = authenticate(request,username=username,password=password)
            if user:
                from django.contrib.auth import login
                login(request,user)
                from django.shortcuts import redirect
                return redirect('/')
            else:
                return render(request,'account/login.html',{'form':form})
        else:
            return render(request,'account/login.html',{'form':form})