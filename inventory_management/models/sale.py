from db.database import execute_query
from decimal import Decimal

def record_sale(product_name, quantity_sold, selling_price):
    """Record a sale and update the product quantity."""
    product_query = "SELECT product_id, price, quantity FROM products WHERE product_name = %s"
    product = execute_query(product_query, (product_name,), fetch=True)
    
    if product and product[0][2] >= quantity_sold:
        product_id = product[0][0]
        cost_price = float(product[0][1])  # Convert Decimal to float
        total_amount = selling_price * quantity_sold
        profit = (selling_price - cost_price) * quantity_sold
        new_quantity = product[0][2] - quantity_sold

        sale_query = "INSERT INTO sales (product_id, sale_date, sale_time, quantity_sold, total_amount, profit) VALUES (%s, CURDATE(), CURTIME(), %s, %s, %s)"
        execute_query(sale_query, (product_id, quantity_sold, total_amount, profit))

        update_query = "UPDATE products SET quantity = %s WHERE product_id = %s"
        execute_query(update_query, (new_quantity, product_id))
        print("Sale recorded successfully!")
    else:
        print("Insufficient quantity available.")

def show_sales():
    sales_query = "SELECT * FROM sales"
    return execute_query(sales_query, fetch=True)