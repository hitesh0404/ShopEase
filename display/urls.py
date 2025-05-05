from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]