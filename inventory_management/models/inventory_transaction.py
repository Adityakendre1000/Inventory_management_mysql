from db.database import execute_query

def add_inventory_transaction(product_id, transaction_type, quantity, reason):
    query = "INSERT INTO inventory_transactions (product_id, transaction_date, transaction_type, quantity, reason) VALUES (%s, CURDATE(), %s, %s, %s)"
    execute_query(query, (product_id, transaction_type, quantity, reason))

def show_inventory_transactions():
    query = "SELECT * FROM inventory_transactions"
    return execute_query(query, fetch=True)