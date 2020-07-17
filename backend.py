import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST book (id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer)")
    conn.commit()
    conn.close()