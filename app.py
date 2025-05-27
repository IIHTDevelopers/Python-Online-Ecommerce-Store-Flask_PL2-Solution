from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('store.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    total_value = conn.execute('SELECT SUM(price) FROM products').fetchone()[0]
    conn.close()
    total_value = total_value if total_value else 0
    return render_template('dashboard.html', products=products, total_value=total_value)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', (name, price, description))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        conn.execute('UPDATE products SET name = ?, price = ?, description = ? WHERE id = ?', (name, price, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit_product.html', id=id, name=product['name'], price=product['price'], description=product['description'])

@app.route('/delete_product/<int:id>')
def delete_product(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(p) for p in products])

@app.route('/api/product', methods=['POST'])
def add_product_json():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)',
                 (data['name'], data['price'], data['description']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
