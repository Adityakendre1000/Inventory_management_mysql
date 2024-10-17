from db.database import execute_query

def add_product(product_name, category, quantity, price, supplier_name, contact_details, date, time):
    # Check if product already exists
    product_query = "SELECT product_id, quantity, price FROM products WHERE product_name = %s"
    product = execute_query(product_query, (product_name,), fetch=True)
    
    if product:
        # Update existing product
        product_id = product[0][0]
        existing_quantity = product[0][1]
        existing_price = float(product[0][2])  # Convert Decimal to float
        
        new_quantity = existing_quantity + quantity
        new_price = ((existing_quantity * existing_price) + (quantity * price)) / new_quantity
        
        update_query = "UPDATE products SET quantity = %s, price = %s WHERE product_id = %s"
        execute_query(update_query, (new_quantity, new_price, product_id))
    else:
        # Add new product
        query = "INSERT INTO products (product_name, category, quantity, price) VALUES (%s, %s, %s, %s)"
        execute_query(query, (product_name, category, quantity, price))
    
    # Add supplier
    supplier_query = "INSERT INTO suppliers (supplier_name, contact_details, product_name, quantity, price) VALUES (%s, %s, %s, %s, %s)"
    execute_query(supplier_query, (supplier_name, contact_details, product_name, quantity, price))

def show_products():
    query = "SELECT * FROM products"
    return execute_query(query, fetch=True)

def remove_product(product_id):
    query = "DELETE FROM products WHERE product_id = %s"
    execute_query(query, (product_id,))

def update_product(product_id, product_name, category, quantity, price):
    query = "UPDATE products SET product_name = %s, category = %s, quantity = %s, price = %s WHERE product_id = %s"
    execute_query(query, (product_name, category, quantity, price, product_id))