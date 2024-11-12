from django.urls import path
from .views import order_list, create_order, update_order, delete_order, order_detail

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
    path('update/<int:order_id>/', update_order, name='update_order'),
    path('delete/<int:order_id>/', delete_order, name='delete_order'),
    path('detail/<int:order_id>/', order_detail, name='order_detail'),
]
