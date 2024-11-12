from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import InventoryItem, Supplier, Restock
from .forms import InventoryItemForm, SupplierForm, RestockForm
from django.core.paginator import Paginator

# Inventory CRUD Views
def inventory_list(request):
    inventory_queryset = InventoryItem.objects.all()
    
    paginator = Paginator(inventory_queryset, 1000)
    
    page_number = request.GET.get('page', 1)
    
    inventory_page = paginator.get_page(page_number)
    
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_page})


def inventory_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})

def inventory_update(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm(instance=inventory_item)
    return render(request, 'inventory/inventory_form.html', {'form': form})

def inventory_delete(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'inventory_item': inventory_item})

# Supplier CRUD Views
def supplier_list(request):
    suppliers_queryset = Supplier.objects.all()
    
    paginator = Paginator(suppliers_queryset, 1000)
    
    page_number = request.GET.get('page', 1)
    
    suppliers_page = paginator.get_page(page_number)
    
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers_page})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/supplier_form.html', {'form': form})

def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_list')

def restock_list(request):
    restocks_queryset = Restock.objects.all()
    
    paginator = Paginator(restocks_queryset, 1000)
    
    page_number = request.GET.get('page', 1)
    
    restocks_page = paginator.get_page(page_number)
    
    return render(request, 'inventory/restock_list.html', {'restocks': restocks_page})

# Restock CRUD Views
def restock_create(request):
    if request.method == 'POST':
        form = RestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restock_list')  
    else:
        form = RestockForm()
    return render(request, 'inventory/restock_form.html', {'form': form})

def restock_update(request, pk):
    restock = get_object_or_404(Restock, pk=pk)
    if request.method == 'POST':
        form = RestockForm(request.POST, instance=restock)
        if form.is_valid():
            form.save()
            return redirect('restock_list')
    else:
        form = RestockForm(instance=restock)
    return render(request, 'inventory/restock_form.html', {'form': form})

def restock_delete(request, pk):
    restock = get_object_or_404(Restock, pk=pk)
    restock.delete()
    return redirect('restock_list')


# Create your views here.
