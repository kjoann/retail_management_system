from faker import Faker
import random
from customers.models import Customer
from products.models import Product
from orders.models import Order, OrderItem

fake = Faker()

def generate_customers():
    try:
        customers = []
        for _ in range(50):
            customers.append(Customer(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:15],
                address=fake.address()
            ))
        Customer.objects.bulk_create(customers)
        print("50 fake customers created successfully!")
    except Exception as e:
        print(f"Error creating customers: {e}")

def generate_products():
    try:
        products = []
        for _ in range(50):
            products.append(Product(
                name=fake.word().capitalize(),
                description=fake.sentence(),
                price=round(random.uniform(5.0, 500.0), 2)
            ))
        Product.objects.bulk_create(products)
        print("50 fake products created successfully!")
    except Exception as e:
        print(f"Error creating products: {e}")

def generate_orders_and_items():
    try:
        customers = Customer.objects.all()
        products = Product.objects.all()
        
        # Generate Orders
        orders = []
        for _ in range(50):
            orders.append(Order(
                customer=random.choice(customers),
                status=random.choice(['pending', 'completed'])
            ))
        Order.objects.bulk_create(orders)
        print("50 fake orders created successfully!")

        # Generate Order Items
        order_items = []
        for order in Order.objects.all():
            for _ in range(random.randint(1, 5)):  # Each order has 1-5 items
                order_items.append(OrderItem(
                    order=order,
                    product=random.choice(products),
                    quantity=random.randint(1, 10)
                ))
        OrderItem.objects.bulk_create(order_items)
        print("Order items created successfully!")
    except Exception as e:
        print(f"Error creating orders or order items: {e}")

if __name__ == "__main__":
    print("Generating fake data for the Retail Management System...")
    generate_customers()
    generate_products()
    generate_orders_and_items()
    print("All fake data generated successfully!")
