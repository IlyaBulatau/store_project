from django.db import models
from django.contrib.auth.models import User


from product.models import Product

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=1)
    active = models.BooleanField(default=True)

    def str(self):
        return self.content