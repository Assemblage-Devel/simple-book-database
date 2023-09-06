from .db_connection import DatabaseConnection

"""
Concerened with storing, retrieving, editing and deleting books from sqlite database

"""
host = "data.db"

def create_book_table():
    with DatabaseConnection(host) as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
        


def add_book(name, author):
    """
    function adds provided book entry to database
    """
    with DatabaseConnection(host) as connection:
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO books VALUES(?, ?, 0)",(name, author))


def get_books():
    """
    function retrieves entries from database
    """
    with DatabaseConnection(host) as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        # books = cursor.fetchall() # list of tupples [(name,author,read),(..),(..)]
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books
    
    
def mark_book(name, author):
    """
    function marks provided entry in database to read: True
    """
    with DatabaseConnection(host) as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=? AND author=?", (name, author))


def del_book(name, author):
    """
    function removes provided entry from database
    """
    with DatabaseConnection(host) as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=? AND author=?", (name, author))




