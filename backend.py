import sqlite3

def connect():
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER,
            ISBN INTEGER )""")
    conn.commit()
    conn.close()

def add_entry(title,author,year,isbn):
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (Null,?,?,?,?)",(title, author,year,isbn))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    row = cur.fetchall()
    conn.close()
    return row

def search_all(title="",author="",year="",isbn=""):
    # passing enpty strings as default so that if user passes only one entry rest will be empty default
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year,isbn))
    row = cur.fetchall()
    conn.close()
    return row

def delete_all(id):
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_data(id,title,author,year,isbn):
    conn = sqlite3.connect('book_store.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET  title = ?, author =?, year =?,isbn = ? WHERE id=?", (title, author,year,isbn, id))
    conn.commit()
    conn.close()



#update_data(3, 'baddie book', 'butty-butter',1992, 345666)
#delete_all(2)
#connect()    
#add_entry('bokie book', 'butty-butter', '1992','345678')
#print(view_all())
