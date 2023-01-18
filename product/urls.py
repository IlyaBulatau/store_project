from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('cat/<int:category_id>/', views.cat_detail, name='cat_detail'),
    path('<int:pk>/', views.post_detail, name='product'),
    path('cat/<int:category_id>/<int:pk>/', views.post_detail, name='product'),

]