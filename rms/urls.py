from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    # path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('', include('inventory.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),

]
