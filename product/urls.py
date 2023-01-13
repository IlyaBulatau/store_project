from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('<int:pk>/', views.ProductDeatailView.as_view(), name='product')
]