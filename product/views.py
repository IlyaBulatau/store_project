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


def post_detail(request, pk, category_id):
    template_name = 'product/product.html'
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,})


def cat_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/cat_detail.html',
         {'category': category, 'page_obj': page_obj})


