from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

examples = Blueprint('examples', __name__)


def validate_quantity(quantity_str):
    """
    Validate that quantity is a non-negative integer.
    Business rule: Stock quantity must always be zero or greater.

    Returns (is_valid, quantity_int, error_message)
    """
    try:
        quantity = int(quantity_str) if quantity_str else 0
        if quantity < 0:
            return False, 0, "Quantity must be zero or greater."
        return True, quantity, None
    except ValueError:
        return False, 0, "Quantity must be a valid number."


def validate_price(price_str):
    """
    Validate that price is a non-negative number.

    Returns (is_valid, price_float, error_message)
    """
    try:
        price = float(price_str) if price_str else 0.0
        if price < 0:
            return False, 0.0, "Price must be zero or greater."
        return True, price, None
    except ValueError:
        return False, 0.0, "Price must be a valid number."


def validate_name(name_str):
    """
    Validate that name is not empty or whitespace-only.

    Returns (is_valid, cleaned_name, error_message)
    """
    if not name_str:
        return False, "", "Name is required."
    cleaned = name_str.strip()
    if not cleaned:
        return False, "", "Name cannot be empty or whitespace only."
    return True, cleaned, None


# ============================================================
# Products CRUD
# ============================================================

@examples.route('/', methods=['GET', 'POST'])
def show_examples():
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return render_template('examples.html', all_products=[], all_collections=[], all_orders=[])
    cursor = db.cursor()

    # Handle POST request to add a new product
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        price = request.form['price']
        sku = request.form.get('sku', '')
        quantity = request.form.get('quantity', '0')
        collection_id = request.form.get('collection_id') or None
        is_active = 1 if request.form.get('is_active') else 0

        # Validate name
        is_valid, name, error = validate_name(name)
        if not is_valid:
            flash(error, 'danger')
            return redirect(url_for('examples.show_examples'))

        # Validate quantity (business rule: must be >= 0)
        is_valid, quantity_int, error = validate_quantity(quantity)
        if not is_valid:
            flash(error, 'danger')
            return redirect(url_for('examples.show_examples'))

        # Validate price
        is_valid, price_float, error = validate_price(price)
        if not is_valid:
            flash(error, 'danger')
            return redirect(url_for('examples.show_examples'))

        cursor.execute(
            'INSERT INTO products (name, description, price, sku, quantity, collection_id, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (name, description, price_float, sku, quantity_int, collection_id, is_active)
        )
        db.commit()

        flash('New product added successfully!', 'success')
        return redirect(url_for('examples.show_examples'))

    # Handle GET request to display all data
    cursor.execute('SELECT * FROM products ORDER BY id DESC')
    all_products = cursor.fetchall()

    cursor.execute('SELECT * FROM collections ORDER BY id')
    all_collections = cursor.fetchall()

    cursor.execute('SELECT * FROM orders ORDER BY id DESC')
    all_orders = cursor.fetchall()

    return render_template('examples.html',
                           all_products=all_products,
                           all_collections=all_collections,
                           all_orders=all_orders)


@examples.route('/update_product/<int:product_id>', methods=['POST'])
def update_product(product_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    name = request.form['name']
    description = request.form.get('description', '')
    price = request.form['price']
    sku = request.form.get('sku', '')
    quantity = request.form.get('quantity', '0')
    collection_id = request.form.get('collection_id') or None
    is_active = 1 if request.form.get('is_active') else 0

    # Validate name
    is_valid, name, error = validate_name(name)
    if not is_valid:
        flash(error, 'danger')
        return redirect(url_for('examples.show_examples'))

    # Validate quantity (business rule: must be >= 0)
    is_valid, quantity_int, error = validate_quantity(quantity)
    if not is_valid:
        flash(error, 'danger')
        return redirect(url_for('examples.show_examples'))

    # Validate price
    is_valid, price_float, error = validate_price(price)
    if not is_valid:
        flash(error, 'danger')
        return redirect(url_for('examples.show_examples'))

    cursor.execute(
        'UPDATE products SET name = %s, description = %s, price = %s, sku = %s, quantity = %s, collection_id = %s, is_active = %s WHERE id = %s',
        (name, description, price_float, sku, quantity_int, collection_id, is_active, product_id)
    )
    db.commit()

    flash('Product updated successfully!', 'success')
    return redirect(url_for('examples.show_examples'))


@examples.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
    db.commit()

    flash('Product deleted successfully!', 'danger')
    return redirect(url_for('examples.show_examples'))


# ============================================================
# Collections CRUD
# ============================================================

@examples.route('/add_collection', methods=['POST'])
def add_collection():
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    name = request.form['name']
    description = request.form.get('description', '')

    # Validate name
    is_valid, name, error = validate_name(name)
    if not is_valid:
        flash(error, 'danger')
        return redirect(url_for('examples.show_examples'))

    cursor.execute(
        'INSERT INTO collections (name, description) VALUES (%s, %s)',
        (name, description)
    )
    db.commit()

    flash('New collection added successfully!', 'success')
    return redirect(url_for('examples.show_examples'))


@examples.route('/update_collection/<int:collection_id>', methods=['POST'])
def update_collection(collection_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    name = request.form['name']
    description = request.form.get('description', '')

    # Validate name
    is_valid, name, error = validate_name(name)
    if not is_valid:
        flash(error, 'danger')
        return redirect(url_for('examples.show_examples'))

    cursor.execute(
        'UPDATE collections SET name = %s, description = %s WHERE id = %s',
        (name, description, collection_id)
    )
    db.commit()

    flash('Collection updated successfully!', 'success')
    return redirect(url_for('examples.show_examples'))


@examples.route('/delete_collection/<int:collection_id>', methods=['POST'])
def delete_collection(collection_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    # CASCADE DELETE will automatically delete associated products
    cursor.execute('DELETE FROM collections WHERE id = %s', (collection_id,))
    db.commit()

    flash('Collection deleted successfully! Associated products were also removed.', 'danger')
    return redirect(url_for('examples.show_examples'))


# ============================================================
# Orders CRUD
# ============================================================

@examples.route('/add_order', methods=['POST'])
def add_order():
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    customer_name = request.form['customer_name']
    customer_email = request.form.get('customer_email', '')
    customer_phone = request.form.get('customer_phone', '')
    shipping_address = request.form.get('shipping_address', '')
    order_total = request.form['order_total']
    status = request.form.get('status', 'pending')

    # Validate customer name
    is_valid, customer_name, error = validate_name(customer_name)
    if not is_valid:
        flash('Customer name is required.', 'danger')
        return redirect(url_for('examples.show_examples'))

    # Validate order total
    is_valid, total_float, error = validate_price(order_total)
    if not is_valid:
        flash('Order total must be a valid non-negative number.', 'danger')
        return redirect(url_for('examples.show_examples'))

    cursor.execute(
        'INSERT INTO orders (customer_name, customer_email, customer_phone, shipping_address, order_total, status) VALUES (%s, %s, %s, %s, %s, %s)',
        (customer_name, customer_email, customer_phone, shipping_address, total_float, status)
    )
    db.commit()

    flash('New order added successfully!', 'success')
    return redirect(url_for('examples.show_examples'))


@examples.route('/update_order/<int:order_id>', methods=['POST'])
def update_order(order_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    customer_name = request.form['customer_name']
    customer_email = request.form.get('customer_email', '')
    customer_phone = request.form.get('customer_phone', '')
    shipping_address = request.form.get('shipping_address', '')
    order_total = request.form['order_total']
    status = request.form.get('status', 'pending')

    # Validate customer name
    is_valid, customer_name, error = validate_name(customer_name)
    if not is_valid:
        flash('Customer name is required.', 'danger')
        return redirect(url_for('examples.show_examples'))

    # Validate order total
    is_valid, total_float, error = validate_price(order_total)
    if not is_valid:
        flash('Order total must be a valid non-negative number.', 'danger')
        return redirect(url_for('examples.show_examples'))

    cursor.execute(
        'UPDATE orders SET customer_name = %s, customer_email = %s, customer_phone = %s, shipping_address = %s, order_total = %s, status = %s WHERE id = %s',
        (customer_name, customer_email, customer_phone, shipping_address, total_float, status, order_id)
    )
    db.commit()

    flash('Order updated successfully!', 'success')
    return redirect(url_for('examples.show_examples'))


@examples.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    db = get_db()
    if db is None:
        flash('Database connection failed. Please try again later.', 'danger')
        return redirect(url_for('examples.show_examples'))
    cursor = db.cursor()

    # CASCADE DELETE will automatically delete associated order items
    cursor.execute('DELETE FROM orders WHERE id = %s', (order_id,))
    db.commit()

    flash('Order deleted successfully!', 'danger')
    return redirect(url_for('examples.show_examples'))
