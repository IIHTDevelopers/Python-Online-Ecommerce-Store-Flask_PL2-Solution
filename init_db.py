import sqlite3

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database initialized!")

if __name__ == '__main__':
    init_db()
