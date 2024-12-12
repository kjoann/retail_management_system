from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.http import JsonResponse

def product_list(request):
    # products = Product.objects.all().order_by('id') # Retrieve all products
    # paginator = Paginator(products, 10)  # Show 10 products per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)  # Get the appropriate page

    # # return render(request, 'products/list.html', {'page_obj': page_obj})
    # products_data = list(page_obj.object_list.values('id', 'name', 'description', 'price'))
    
    # # Return the data as JSON
    # return JsonResponse({'products': products_data, 'page': page_number, 'total_pages': paginator.num_pages})
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    
    return JsonResponse({'products': list(products)})

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
