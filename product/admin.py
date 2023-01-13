from django.contrib import admin

from .models import Category, Product, Description

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    list_display_links = ['id', 'title']

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Description)
