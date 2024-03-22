from bookstoreClass import Author, Book
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

def setTable():
    Author.createTable(cursor, conn)
    Book.createTable(cursor, conn)
   
def add_book(title, publication_year, author_id):
    # Add a new book to the database
    cursor.execute("INSERT INTO books (title, publication_year, author_id) VALUES (?, ?, ?)", (title, publication_year, author_id))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print(f"-----Book added successfully.------")
    print("\033[92m*\033[0m" * 100)


