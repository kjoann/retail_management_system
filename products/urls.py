# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Change this to match the root URL
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('<int:product_id>/update/', views.product_update, name='product_update'),
    path('<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
