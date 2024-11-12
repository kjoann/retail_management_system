from django.db import models
# from products.models import Product 

class Customer(models.Model):
    name = models.CharField(max_length=255)  # Stores the customer's name
    email = models.EmailField(unique=True)   # Stores email 
    phone_number = models.CharField(max_length=15)  # Stores the customer's phone number
    address = models.TextField()  # Stores their address
    # products = models.ManyToManyField(Product, through='Purchase', related_name='customers')
    
    class Meta:
        db_table = 'customers_table'

    def __str__(self):
        return self.name  

# Create your models here.
