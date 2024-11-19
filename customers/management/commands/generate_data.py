from django.core.management.base import BaseCommand
from customers.models import Customer
from products.models import Product
from orders.models import Order, OrderItem
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake data for the retail management system'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate Customers
        customers = []
        for _ in range(50):
            customers.append(Customer(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:15],
                address=fake.address()
            ))
        Customer.objects.bulk_create(customers)
        self.stdout.write("50 fake customers created!")

        # Generate Products
        products = []
        for _ in range(50):
            products.append(Product(
                name=fake.word().capitalize(),
                description=fake.sentence(),
                price=round(random.uniform(5.0, 500.0), 2)
            ))
        Product.objects.bulk_create(products)
        self.stdout.write("50 fake products created!")

        # Generate Orders and Order Items
        customers = Customer.objects.all()
        products = Product.objects.all()
        orders = []
        for _ in range(50):
            orders.append(Order(
                customer=random.choice(customers),
                status=random.choice(['pending', 'completed'])
            ))
        Order.objects.bulk_create(orders)
        self.stdout.write("50 fake orders created!")

        order_items = []
        for order in Order.objects.all():
            for _ in range(random.randint(1, 5)):
                order_items.append(OrderItem(
                    order=order,
                    product=random.choice(products),
                    quantity=random.randint(1, 10)
                ))
        OrderItem.objects.bulk_create(order_items)
        self.stdout.write("Order items created successfully!")
