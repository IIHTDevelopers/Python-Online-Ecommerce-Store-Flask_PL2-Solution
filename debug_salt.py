from app import get_db_connection

conn = get_db_connection()
cursor = conn.execute("SELECT price FROM products WHERE name = ?", ("salt",))
row = cursor.fetchone()
conn.close()

print(f"Row found: {row}")
if row:
    print(f"Price: {row['price']}")
    print(f"Price type: {type(row['price'])}")
    print(f"Price == 100: {row['price'] == 100}")
    print(f"Price is not None: {row is not None}")
    print(f"Combined result: {row is not None and row['price'] == 100}")
else:
    print("No row found")
