import sqlite3

class DatabaseConnection():
    def __init__(self,filename):
        self.conn = None
        self.filename = filename
    
    def __enter__(self):
        self.conn= sqlite3.connect(self.filename)
        print("connection created!")
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
        self.conn.close()
        print("connection closed!")

if __name__ == "__main__":
    with DatabaseConnection("TESTDATABASE.DB") as connection:
        cursor = connection.cursor()
        a =cursor.execute("""
                       SELECT * FROM dbCache
                       """).fetchall()
        print(type(connection))