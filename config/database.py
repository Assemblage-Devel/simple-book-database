import json

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
    with open(books_file, "w") as file:
        json.dump([],file)


def add_book(name, author):
    """
    function adds provided book entry to database
    """

    books = get_books()
    books.append({"name": name, "author": author, "read": False})
    _save_all_books(books)


def get_books():
    """
    function retrieves entries from database
    """

    with open(books_file, "r") as file:
        return json.load(file) # returns a list of dics
    

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




