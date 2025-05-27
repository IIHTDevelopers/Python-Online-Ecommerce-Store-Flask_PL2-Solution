import sqlite3

conn = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row

print("All products in database:")
cursor = conn.execute('SELECT * FROM products')
products = cursor.fetchall()

for product in products:
    print(f"ID: {product['id']}, Name: '{product['name']}', Price: {product['price']}, Description: {product['description']}")

print(f"\nTotal products: {len(products)}")

# Check specifically for Salt (both cases)
print("\nChecking for salt products:")
salt_cursor = conn.execute("SELECT * FROM products WHERE name = 'Salt'")
salt_product = salt_cursor.fetchone()

if salt_product:
    print(f"Salt (uppercase) found: Price = {salt_product['price']}")
else:
    print("No Salt (uppercase) product found")

salt_lower_cursor = conn.execute("SELECT * FROM products WHERE name = 'salt'")
salt_lower_product = salt_lower_cursor.fetchone()

if salt_lower_product:
    print(f"salt (lowercase) found: Price = {salt_lower_product['price']}")
else:
    print("No salt (lowercase) product found")

conn.close()
