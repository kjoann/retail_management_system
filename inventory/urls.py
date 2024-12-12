from django.urls import path
from . import views


urlpatterns = [
    # Inventory CRUD URLs
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/create/', views.inventory_create, name='inventory_create'),
    path('inventory/update/<int:pk>/', views.inventory_update, name='inventory_update'),
    path('inventory/delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),

    # Supplier CRUD URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/update/<int:pk>/', views.supplier_update, name='supplier_update'),
    path('suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),

    # Restock CRUD URLs
    path('restocks/', views.restock_list, name='restock_list'),
    path('restocks/create/', views.restock_create, name='restock_create'),
    path('restocks/update/<int:pk>/', views.restock_update, name='restock_update'),
    path('restocks/delete/<int:pk>/', views.restock_delete, name='restock_delete'),
    
    path('insights/', views.inventory_insights, name='inventory_insights'),
]
