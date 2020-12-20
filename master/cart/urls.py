from django.urls import path

from .views import show_cart, add_cart, delete_from_cart, decrement_cart,confirmation

urlpatterns = [
    path('show_cart/', show_cart, name='show_cart'),
    
    path('add_cart/<int:service_id>', add_cart, name="add_cart"),
    path('decrement_cart/<int:service_id>', decrement_cart, name="decrement_cart"),
    path('confirmation/',confirmation , name="confirmation"),
    path('delete_from_cart/<int:service_id>',
         delete_from_cart, name="delete_from_cart"),
]