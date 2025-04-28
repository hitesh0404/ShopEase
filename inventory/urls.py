from django.urls import path
from . import views
urlpatterns = [
    path('product-list/',views.product_list,name='product_list'),
    path('product/create/',views.ProductCreate.as_view(),name='product_create'),
    path('product-detail/<int:id>/',views.product_detail,name='product_detail'),
    path('product-delete/<int:id>/',views.product_delete,name='product_delete'),
    path('product-update/<int:id>/',views.ProductUpdate.as_view(),name='product_update'),
]