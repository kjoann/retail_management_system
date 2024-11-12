from django import forms
from .models import InventoryItem, Supplier, Restock

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['product', 'quantity', 'location']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class RestockForm(forms.ModelForm):
    class Meta:
        model = Restock
        fields = ['product', 'quantity', 'supplier']
