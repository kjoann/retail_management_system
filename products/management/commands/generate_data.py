from products.models import Product
from customers.models import Customer
from random import choice, randint
from decimal import Decimal

# Sample data for generating random products and customers
first_names = ["Rita", "Joanna", "Celia", "Honorine", "Kellia", "Latifah", "Blaise", "Regis", "Audrey", "Joella"]
last_names = ["Umutoni", "Cyiza", "Tito", "Kaze", "Shema", "Ganza", "Uwineza", "Keza", "Kamali", "Kamana"]
address_names = ["Kicukiro", "Nyabihu", "Musanze", "Nyarugenge", "Gasabo", "Rwamagana", "Nyagatare", "Ruhengeri"]

customers = []

# Generate 500,000 random products and customers
for _ in range(500000):

    # Generate random customer
    first_name = choice(first_names)
    last_name = choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone_number = f"+1{randint(1000000000, 9999999999)}"
    address = choice(address_names)
    customer = Customer(name=f"{first_name} {last_name}", email=email, phone_number=phone_number, address=address)
    customers.append(customer)


Customer.objects.bulk_create(customers)

print("Successfully created 500,000 records.")

