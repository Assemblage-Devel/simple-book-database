"""
Concerened with storing, retrieving, editing and deleting books from the 'in memory' database
"""

books = []

def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})


def list_books():
    for book in books:
        print(f"{book['name']} by {book['author']}")

def mark_book(name, author):
    pass


def del_book(name, author):
    pass

