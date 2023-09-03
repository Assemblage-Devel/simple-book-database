"""
Concerened with storing, retrieving, editing and deleting books from the 'in memory' database
"""

books = []

def add_book(name, author):
    """
    function adds provided book entry to database
    """
    books.append({"name": name, "author": author, "read": False})


def list_books():
    """
    function lists formatted entries in database
    """
    for book in books:
        read = "YES" if book["read"] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")

def mark_book(name, author):
    """
    function marks provided entry in database to read: True
    """
    for book in books:
        if book["name"] and  book["author"] == name and author:
            book["read"] = True
        else:
            pass


def del_book(name, author):
    """
    function removes provided entry from database
    """
    global books

    books = [book for book in books if book["name"] != name and book["author"] != author]




