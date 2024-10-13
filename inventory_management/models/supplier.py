from db.database import execute_query

def add_supplier(supplier_name, contact_details, product_name, quantity, price):
    query = "INSERT INTO suppliers (supplier_name, contact_details, product_name, quantity, price) VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, (supplier_name, contact_details, product_name, quantity, price))

def show_suppliers():
    query = "SELECT * FROM suppliers"
    return execute_query(query, fetch=True)

def remove_supplier(supplier_id):
    query = "DELETE FROM suppliers WHERE supplier_id = %s"
    execute_query(query, (supplier_id,))