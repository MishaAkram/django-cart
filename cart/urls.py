# cart/urls.py
from django.urls import path
from .views import product_list, view_cart, add_to_cart

urlpatterns = [    
    path('products/', product_list, name='product_list'),
    path('cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
