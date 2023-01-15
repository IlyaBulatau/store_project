from django.db import models

from product.models import Product

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    products = models.ManyToManyField(Product, through='CartProduct')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_id


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def sub_total(self):
            return self.product.price * self.quantity

    def __str__(self):
        return self.product