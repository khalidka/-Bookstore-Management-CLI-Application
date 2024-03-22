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


def view_books():
    # View all books with their respective authors
    cursor.execute("SELECT b.id, b.title, b.publication_year, a.name FROM books b JOIN authors a ON b.author_id = a.id")
    books = cursor.fetchall()
    if not books:
        print("No books found in the inventory.")
    else:
        print("\033[92m*\033[0m" * 100)
        print("Books in the inventory:")
        print("\033[94m-\033[0m" * 50)
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Year: {book[2]}, Author: {book[3]}")
    print("\033[92m*\033[0m" * 100)


def update_book(book_id, title, publication_year, author_id):
    # Update an existing book in the database
    cursor.execute("UPDATE books SET title=?, publication_year=?, author_id=? WHERE id=?", (title, publication_year, author_id, book_id))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print(f"Book with ID {book_id} updated successfully.")
    print("\033[92m*\033[0m" * 100)

def delete_book(book_id):
    # Delete a book from the database
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print(f"Book with ID {book_id} deleted successfully.")
    print("\033[92m*\033[0m" * 100)

def add_author(name):
    # Add a new author to the database
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print("Author added successfully.")
    print("\033[92m*\033[0m" * 100)    

def view_authors():
    # View all authors in the database
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    if not authors:
        print("No authors found.")
    else:
        print("\033[92m*\033[0m" * 100)
        print("Authors:")
        print("\033[94m-\033[0m" * 50)
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}")
    print("\033[92m*\033[0m" * 100)  

def update_author(author_id, name):
    # Update an existing author in the database
    cursor.execute("UPDATE authors SET name=? WHERE id=?", (name, author_id))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print(f"Author with ID {author_id} updated successfully.")
    print("\033[92m*\033[0m" * 100)   

def delete_author(author_id):
    # Delete an author from the database
    cursor.execute("DELETE FROM authors WHERE id=?", (author_id,))
    conn.commit()
    print("\033[92m*\033[0m" * 100)
    print(f"Author with ID {author_id} deleted successfully.")
    print("\033[92m*\033[0m" * 100)



print("\033[92m*\033[0m" * 100)       