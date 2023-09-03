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
    name = input("Book Title: ")
    author = input("Author: ")
    db.add_book(name, author)


def list_books():
    db.list_books()


def mark_book():
    name = input("Book Title: ")
    author = input("Author: ")
    db.mark_book(name, author)


def del_book():
    name = input("Book Title: ")
    author = input("Author: ")
    db.del_book(name, author)


menu()