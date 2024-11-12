from django.db import models
from products.models import Product  # Assuming Product app is named "products"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=200, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

class Restock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    restock_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Restock: {self.product.name} - {self.quantity} units"


# Create your models here.
