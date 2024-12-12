import requests
import pandas as pd

try:
    product_api = requests.get('http://127.0.0.1:8000/products/')
    product_api.raise_for_status()
    product_api_data = product_api.json() 
    
    customers_api = requests.get('http://127.0.0.1:8000/customers/')
    customers_api.raise_for_status()
    customers_api_data = customers_api.json()
    
    df1 = pd.DataFrame(product_api_data['products'])
    df2 = pd.DataFrame(customers_api_data['customers'])
    
    
    print(f"DataFrame shape (rows, columns): {df1.shape}")
    print(f"DataFrame shape (rows, columns): {df2.shape}")
    

    # Export the first 50 customers
    df2.iloc[:50].to_csv('customers_1.csv', index=False, mode='w', header=True)
    print("Exported first 50 customers to customers_1.csv")

    # Export the next 50 customers
    df2.iloc[50:100].to_csv('customers_2.csv', index=False, mode='w', header=True)
    print("Exported next 50 customers to customers_2.csv")

    # Read the two CSV files into DataFrames
    customer_df1 = pd.read_csv('customers_1.csv')
    customer_df2 = pd.read_csv('customers_2.csv')
    
    combined_df = pd.concat([customer_df1, customer_df2], ignore_index=True)

    combined_df.to_csv('final_customers.csv', index=False)
    print("Merged both chunks into final_customers.csv")
    
    # Exporting first 50 customers with specific attributes 
    df_part1 = df2[['name', 'email']].iloc[:50]
    df_part1.to_csv('customers_part1.csv', index=False, mode='w', header=True)
    print("Exported first 50 customers with 'name' and 'email' to customers_part1.csv")

    df_part2 = df2[['phone_number', 'address']].iloc[50:100]
    df_part2.to_csv('customers_part2.csv', index=False, mode='w', header=True)
    print("Exported next 50 customers with 'phone_number' and 'address' to customers_part2.csv")

    df1_part = pd.read_csv('customers_part1.csv')
    df2_part = pd.read_csv('customers_part2.csv')

    combined_parts = pd.concat([df1_part, df2_part], axis=1)

    combined_parts.to_csv('final_parts_customers.csv', index=False)
    print("Merged both parts into final_parts_customers.csv")

    
except requests.exceptions.RequestException as e:
    print(f"Error data from API: {e}")