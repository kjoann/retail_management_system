from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator

def product_list(request):
    products_queryset = Product.objects.all()
    
    paginator = Paginator(products_queryset, 1000)
    
    page_number = request.GET.get('page', 1)
    
    products_page = paginator.get_page(page_number)
    
    return render(request, 'products/list.html', {'products': products_page})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create.html', {'form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete.html', {'product': product})


# Create your views here.
