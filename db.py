import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, quantity text, part text, specs text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, quantity, part, specs, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (quantity, part, specs, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, specs, quantity, price):
        self.cur.execute("UPDATE parts SET quantity = ?, part = ?, specs = ?, price = ? WHERE id = ?", (quantity, part, specs, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')
