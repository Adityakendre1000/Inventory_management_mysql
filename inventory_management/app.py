from flask import Flask, render_template, request, redirect, url_for
from models.product import add_product, show_products, remove_product, update_product
from models.sale import record_sale, show_sales
from models.supplier import add_supplier, show_suppliers, remove_supplier
from models.inventory_transaction import add_inventory_transaction, show_inventory_transactions

app = Flask(__name__)

@app.route('/')
def index():
    products = show_products()
    sales = show_sales()
    suppliers = show_suppliers()
    inventory_transactions = show_inventory_transactions()
    return render_template('index.html', products=products, sales=sales, suppliers=suppliers, inventory_transactions=inventory_transactions)

@app.route('/add_product', methods=['POST'])
def add_product_route():
    product_name = request.form['product_name']
    category = request.form['category']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    supplier_name = request.form['supplier_name']
    contact_details = request.form['contact_details']
    
    add_product(product_name, category, quantity, price, supplier_name, contact_details)
    add_supplier(supplier_name, contact_details, product_name, quantity, price)
    return redirect(url_for('index'))

@app.route('/remove_product/<int:product_id>')
def remove_product_route(product_id):
    remove_product(product_id)
    return redirect(url_for('index'))

@app.route('/record_sale', methods=['POST'])
def record_sale_route():
    product_name = request.form['product_name']
    quantity_sold = int(request.form['quantity_sold'])
    selling_price = float(request.form['selling_price'])
    
    record_sale(product_name, quantity_sold, selling_price)
    return redirect(url_for('index'))

@app.route('/remove_supplier/<int:supplier_id>')
def remove_supplier_route(supplier_id):
    remove_supplier(supplier_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)