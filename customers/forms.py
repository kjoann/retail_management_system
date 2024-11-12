from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        # widgets = {
        #     'address': forms.TextInput(attrs={'size': 40}),  # Adjust the 'size' attribute
        # }
