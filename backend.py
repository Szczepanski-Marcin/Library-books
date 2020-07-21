import sqlite3

class Database:

    def __init__(self, db):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer)")
        conn.commit()
        conn.close()

    def insert(swlf, title, author, year, ISBN):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, ISBN))
        conn.commit()
        conn.close()

    def view(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def search(self, title="", author="", year="", ISBN=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=? ", (title, author, year, ISBN))
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self, id,title, author, year, ISBN):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?",(title, author, year, ISBN, id))
        conn.commit()
        conn.close()



#insert("The ssun", "John Smith", 1918, 91312121)
#delete(3)
#update(4, "The SUN", "John Samonta", 2020, 99999999)
#print(view())
#print(search(author="John Smith"))