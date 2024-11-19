from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
from django.forms import modelformset_factory
from django.core.paginator import Paginator

def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/order_list.html', {'page_obj': page_obj})

def create_order(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1)
        formset = OrderItemFormSet(request.POST)
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            for form in formset:
                if form.cleaned_data:
                    order_item = form.save(commit=False)
                    order_item.order = order
                    order_item.save()
            return redirect('order_list')
    else:
        order_form = OrderForm()
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1)
        formset = OrderItemFormSet(queryset=OrderItem.objects.none())
    return render(request, 'orders/create_order.html', {'order_form': order_form, 'formset': formset})

def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=0)  # Set extra=0 to not add additional empty fields
    if request.method == "POST":
        order_form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, queryset=order.items.all())
        if order_form.is_valid() and formset.is_valid():
            order_form.save()
            formset.save()
            return redirect('order_list')
    else:
        order_form = OrderForm(instance=order)
        formset = OrderItemFormSet(queryset=order.items.all())
    
    return render(request, 'orders/update_order.html', {'order_form': order_form, 'formset': formset})


def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/delete_order.html', {'order': order})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


# Create your views here.
