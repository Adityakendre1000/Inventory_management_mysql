from flask import Flask, render_template, request, redirect, url_for
from models.product import add_product, show_products, remove_product
from models.sale import record_sale, show_sales
from models.supplier import add_supplier, show_suppliers, remove_supplier
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('add_product_page'))

@app.route('/add_product_page')
def add_product_page():
    return render_template('add_product.html')

@app.route('/products_page')
def products_page():
    products = show_products()
    return render_template('products.html', products=products)

@app.route('/record_sale_page')
def record_sale_page():
    products = show_products()
    return render_template('record_sale.html', products=products)

@app.route('/sales_records_page')
def sales_records_page():
    sales = show_sales()
    return render_template('sales_records.html', sales=sales)

@app.route('/suppliers_page')
def suppliers_page():
    suppliers = show_suppliers()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/add_product', methods=['POST'])
def add_product_route():
    product_names = request.form.getlist('product_name[]')
    categories = request.form.getlist('category[]')
    quantities = request.form.getlist('quantity[]')
    prices = request.form.getlist('price[]')
    supplier_name = request.form['supplier_name']
    contact_details = request.form['contact_details']
    
    current_datetime = datetime.now()
    date = current_datetime.date()
    time = current_datetime.time()
    
    for product_name, category, quantity, price in zip(product_names, categories, quantities, prices):
        add_product(product_name, category, int(quantity), float(price), supplier_name, contact_details, date, time)
    
    return redirect(url_for('products_page'))

@app.route('/remove_product/<int:product_id>')
def remove_product_route(product_id):
    remove_product(product_id)
    return redirect(url_for('products_page'))

@app.route('/record_sale', methods=['POST'])
def record_sale_route():
    product_names = request.form.getlist('product_name[]')
    quantities_sold = request.form.getlist('quantity_sold[]')
    selling_prices = request.form.getlist('selling_price[]')
    
    current_datetime = datetime.now()
    date = current_datetime.date()
    time = current_datetime.time()
    
    for product_name, quantity_sold, selling_price in zip(product_names, quantities_sold, selling_prices):
        record_sale(product_name, int(quantity_sold), float(selling_price), date, time)
    
    return redirect(url_for('sales_records_page'))

@app.route('/remove_supplier/<int:supplier_id>')
def remove_supplier_route(supplier_id):
    remove_supplier(supplier_id)
    return redirect(url_for('suppliers_page'))

if __name__ == '__main__':
    app.run(debug=True)