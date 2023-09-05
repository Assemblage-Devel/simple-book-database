import sqlite3

"""
Concerened with storing, retrieving, editing and deleting books from json file
Format of the json file:

[
    {
        "name": "title,
        "author": "author",
        "read": True
    }

]
"""


books_file = "books.json"


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

    cursor.execute(f"INSERT INTO books VALUES('{name}', '{author}', 0)")
    
    connection.commit()
    connection.close()


def get_books():
    """
    function retrieves entries from database
    """

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    # cursor.execute("")
    
    connection.commit()
    connection.close()
    

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




