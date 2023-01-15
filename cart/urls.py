from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('<int:product_id>', views.add_cart, name='add_cart'),
]
