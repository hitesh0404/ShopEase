from django.urls import path
from .views import LoginView,RegisterView,my_logout

urlpatterns = [

    path('login/',LoginView.as_view(),name = "login"),
    path('register/',RegisterView.as_view(),name = "register"),
    path('logout/',my_logout,name = "logout"),

    
]