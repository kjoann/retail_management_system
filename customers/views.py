from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create a new customer
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')   
    else:
        form = CustomerForm()
    return render(request, 'customers/create_customer.html', {'form': form})

# List customers (Read)
def customer_list(request):
    # customers = Customer.objects.all()
    # paginator = Paginator(customers, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'customers/customer_list.html', {'page_obj': page_obj})
    customers = Customer.objects.all().values('id', 'name', 'email', 'phone_number', 'address')
    
    return JsonResponse({'customers': list(customers)})


# Update customer
def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/update_customer.html', {'form': form})

# Delete customer
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/delete_customer.html', {'customer': customer})
