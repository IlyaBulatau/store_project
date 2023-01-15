from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartProduct
from product.models import Product

def cart_view(request):
    return render(request, 'cart/cart.html')