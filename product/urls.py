from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name='cat_detail'),
    path('<int:pk>/', views.ProductDeatailView.as_view(), name='product')
]