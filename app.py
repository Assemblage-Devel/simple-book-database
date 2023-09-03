"""
a Books database app with menu
"""

from config import database as db

USER_CHOICE = """

Select an option:
'a' - Add a book to database
'l' - List all books in database
'm' - Mark book as read in database
'd' - Delete book from database
'q' - Quit

Your choice: """


def menu():
    """
    Menu for accessing the database and selecting an operation to execute
    """
    user_input = ' '
    while user_input != 'q':
        user_input = input(USER_CHOICE)
        
        if user_input == 'a':
            add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'm':
            mark_book()

        elif user_input == 'd':
            del_book()

        elif user_input == 'q':
            print("Programme terminated")
            break
        else:
            print("That choice doesn't exist, try again.")


def add_book():
    """
    Add book function - gets user input for title and author,
    function calls to the database to add the entry
    """
    name = input("Book Title: ")
    author = input("Author: ")
    db.add_book(name, author)


def list_books():
    """
    List function retrieves books from the database and prints a formatted 
    list cotaining (title, author, and read status!)
    """
    books = db.get_books()
    for book in books:
        read = "YES" if book["read"] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


def mark_book():
    """
    Mark function - gets user input for title and author,
    function calls database to modify the read status to TRUE
    """
    name = input("Book Title: ")
    author = input("Author: ")
    db.mark_book(name, author)


def del_book():
    """
    Del function - gets user input for title and author,
    function calls database to remove an entry.
    """
    name = input("Book Title: ")
    author = input("Author: ")
    db.del_book(name, author)


menu()