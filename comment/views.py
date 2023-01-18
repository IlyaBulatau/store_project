from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from product.models import Product, Category
from comment.forms import CommentForm
from comment.models import Comment

# def comment(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     form = CommentForm(instance=product)
#     if request.method=='POST':
#         form = CommentForm(data=request.POST, instance=product)
#         if form.is_valid():
#             comment = CommentForm()
#             comment.comments_id = product
#             comment.author_id = auth.get_user(request)
#             comment.content = form.cleaned_data['content']
#             comment.save()
#             return redirect('home')
#     else:
#         form = CommentForm()
#     context = {'form': form, 'product': product}
#     return render(request, 'comment/comments.html', context)
        
