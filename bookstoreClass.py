class Author:
    def __init__(self, name):
        self.name = name

    @classmethod
    def createTable(cls, cursor, CONN):
        query = """
        CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY,
                    name TEXT
        )
        """
        cursor.execute(query)
        CONN.commit()
class Book:
    def __init__(self, title, publication_year, author_id):
        self.title = title
        self.publication_year = publication_year
        self.author_id = author_id

    @classmethod
    def createTable(cls, cursor, CONN):
        query = """
        CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    publication_year INTEGER,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors(id)
        )
        """    
        cursor.execute(query)
        CONN.commit()  