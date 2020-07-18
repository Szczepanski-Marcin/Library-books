import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, ISBN))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="", author="", year="", ISBN=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=? ", (title, author, year, ISBN))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?",(title, author, year, ISBN, id))
    conn.commit()
    conn.close()


connect()
#insert("The ssun", "John Smith", 1918, 91312121)
#delete(3)
#update(4, "The SUN", "John Samonta", 2020, 99999999)
#print(view())
#print(search(author="John Smith"))