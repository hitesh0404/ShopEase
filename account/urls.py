from django.urls import path
from .views import (
    LoginView,
    RegisterView,
    my_logout,
    user_profile)

urlpatterns = [

    path('login/',LoginView.as_view(),name = "login"),
    path('register/',RegisterView.as_view(),name = "register"),
    path('logout/',my_logout,name = "logout"),
    path('user/profile/',user_profile,name='user_profile')
]