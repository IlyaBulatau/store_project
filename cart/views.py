from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartProduct
from product.models import Product

def cart_view(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=cart_view(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_view(request))
        cart.save()
    try:
        cart_item = CartProduct.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartProduct.DoesNotExist:
        cart_item = CartProduct.objects.create(product=product, quantity=1, cart = cart)
        cart_item.save()

    return redirect('cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cart_view(request))
        cart_items = CartProduct.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=cart_view(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartProduct.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=cart_view(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartProduct.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')