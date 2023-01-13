from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Product, Category

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'


class ProductDeatailView(generic.DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'detail'

