"""
Concerened with storing, retrieving, editing and deleting books from json file
Format of the json file:

name,author,read/n
"""

books_file = "books.txt"


def create_book_table():
    with open("books.txt", "w"):
        pass


def add_book(name, author):
    """
    function adds provided book entry to database
    """

    with open(books_file, "a") as file:
        file.write(f"{name},{author},0\n")


def get_books():
    """
    function retrieves entries from database
    """

    with open(books_file, "r") as file:
        lines = [book.strip().split(",") for book in file.readlines()]
    
    return [
        {"name": line[0], "author": line[1], "read": line[2]}
        for line in lines
    ]
    

def mark_book(name, author):
    """
    function marks provided entry in database to read: True
    """

    books = get_books()

    for book in books:
        if book["name"] and  book["author"] == name and author:
            book["read"] = '1'
    _save_all_books(books)


def _save_all_books(books):

    with open(books_file, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def del_book(name, author):
    """
    function removes provided entry from database
    """

    books = get_books()
    books = [book for book in books if book["name"] != name and book["author"] != author]

    _save_all_books(books)




