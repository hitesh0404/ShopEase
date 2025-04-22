from django.urls import path
from . import views
urlpatterns = [
    path('product-list/',views.product_list,name='product_list'),
    path('product/create/',views.product_create,name='product_create'),
    path('product-detail/<int:id>',views.product_detail,name='product_detail'),
]