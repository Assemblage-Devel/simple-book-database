import sqlite3

"""
Concerened with storing, retrieving, editing and deleting books from sqlite database

"""


def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
    
    connection.commit()
    connection.close()


def add_book(name, author):
    """
    function adds provided book entry to database
    """

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books VALUES(?, ?, 0)",(name, author))
    
    connection.commit()
    connection.close()


def get_books():
    """
    function retrieves entries from database
    """

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    # books = cursor.fetchall() # list of tupples [(name,author,read),(..),(..)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()

    return books
    

def _save_all_books(books):

    with open(books_file, "w") as file:
        json.dump(books, file)

    
def mark_book(name, author):
    """
    function marks provided entry in database to read: True
    """

    books = get_books()

    for book in books:
        if book["name"] and  book["author"] == name and author:
            book["read"] = True
    _save_all_books(books)


def del_book(name, author):
    """
    function removes provided entry from database
    """

    books = get_books()
    books = [book for book in books if book["name"] != name and book["author"] != author]

    _save_all_books(books)




