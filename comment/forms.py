from django import forms as f
from django.forms import forms

from comment.models import Comment

class CommentForm(f.ModelForm):
    content = f.CharField(widget=f.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = Comment
        fields = ('content', 'author', 'product')

