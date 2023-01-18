from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views import generic
from django.core.paginator import Paginator

import datetime

from product.models import Product, Category
from comment.forms import CommentForm
from comment.models import Comment

class ProductListView(generic.ListView):
    paginate_by = 3
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'


class ProductDeatailView(generic.DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'detail'

# class CategoryDetailView(generic.DetailView):
#     model = Category
#     template_name = 'product/cat_detail.html'
#     context_object_name = 'category'


def cat_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/cat_detail.html',
         {'category': category, 'page_obj': page_obj})


