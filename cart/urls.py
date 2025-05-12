from django.urls import path
from . import views
urlpatterns = [
    path('add-to-cart/<int:id>/',views.add_to_cart,name="add_to_cart"),
    path('show-cart/',views.show_cart,name="show_cart"),
    path('decrease-quantity/<int:id>/',views.decrease_quantity,name="decrease_cart_quantity"),
    path('increase-quantity/<int:id>/',views.increase_quantity,name="increase_cart_quantity")
]