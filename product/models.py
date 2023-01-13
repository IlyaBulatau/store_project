from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.ForeignKey('Description', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='image')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=None)
    is_published = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Description(models.Model):
    context = [
        ('autumn', 'autumn'),
        ('winter', 'winter'),
        ('spring', 'spring'),
        ('summer', 'summer')
    ]
    color = models.CharField(max_length=50)
    season = models.CharField(max_length=10, choices=context)
    content = models.TextField()

    def __str__(self) -> str:
        return self.color
