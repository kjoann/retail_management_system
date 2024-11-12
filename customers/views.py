from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator


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
    customers_queryset = Customer.objects.all()
    
    paginator = Paginator(customers_queryset, 1000)
    
    page_number = request.GET.get('page', 1)
    
    customers_page = paginator.get_page(page_number)
    
    return render(request, 'customers/customer_list.html', {'customers': customers_page})


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
