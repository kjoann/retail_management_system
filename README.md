# Retail Management System

A Django-based Retail Management System to efficiently manage products, inventory, and customer orders. This system allows users to perform CRUD (Create, Read, Update, Delete) operations across multiple apps, including Products, Inventory, Orders, and Customers.

## Features

- **User Authentication**: Login and Sign-up functionality for secure access.
- **Product Management**: Add, update, and delete products with details like price, stock quantity, and description.
- **Inventory Control**: Keep track of stock levels and manage inventory adjustments.
- **Order Processing**: Create and manage customer orders, view order history.
- **Responsive Design**: Styled using Bootstrap for a clean and responsive UI.
- **PostgreSQL Database**: Uses PostgreSQL for robust data storage.

## Project Structure

```
retail_management_system/
│
├── customers/
├── inventory/
├── orders/
├── products/
├── retail_management_system/
│
├── manage.py
└── .gitignore
```

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- Django

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kjoann/retail_management_system.git
   ```
2. Navigate to the project folder:
   ```bash
   cd retail_management_system
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For MacOS/Linux
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the PostgreSQL database:
   - Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials.

6. Run database migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Sign up or log in to access the management features.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django
- **Database**: PostgreSQL
- **Version Control**: Git and GitHub

## License

This project is open-source and available under the MIT License.
