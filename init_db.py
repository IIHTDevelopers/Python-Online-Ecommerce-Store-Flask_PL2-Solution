import sqlite3

def init_db():
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()

    schema = """
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS products;

    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        description TEXT
    );
INSERT INTO products (name, price, quantity, description) VALUES
      ('Eggs',  50.0, 40, 'Basket of eggs'),
      ('Pen',   50.0, 20, 'Box of pens'),
      ('salt',  40.0, 60, 'Pack of salt'),
      ('Mint',  10.0, 20, 'Pack of mint'),
      ('Gum',   10.0, 10, 'Pack of gum'),
      ('Lays',  10.0, 10, 'Pack of lays');
    """

    cursor.executescript(schema)
    connection.commit()
    connection.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
