from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from product.models import Product, Category
from comment.forms import CommentForm
from comment.models import Comment

def comment(request):
    if request.method=='POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'comment/comments.html', context)
        
