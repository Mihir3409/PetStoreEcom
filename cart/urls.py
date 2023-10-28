from django.urls import path
from .views import add_to_cart,cart_views1,delete_cart,update_cart

urlpatterns = [
    path('add_to_cart/<int:id>', add_to_cart, name="add_to_cart"),
    path('cart_view/',cart_views1, name='cart-view'),
    path('cart_delete/<int:id>/', delete_cart, name='deletecart'),
    path('updatecart/<int:id>/', update_cart,name='updatecart'),
]