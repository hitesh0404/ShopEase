from django.urls import path
from . import views
urlpatterns = [
    path('product-list/',views.product_list),
    path('product/create/',views.product_create),
]