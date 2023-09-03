"""
Concerened with storing, retrieving, editing and deleting books from the 'in memory' database
"""

books = []

def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})


def list_books():
    for book in books:
        read = "YES" if book["read"] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")

def mark_book(name, author):
    for book in books:
        if book["name"] and  book["author"] == name and author:
            book["read"] = True
        else:
            pass


def del_book(name, author):
    pass

