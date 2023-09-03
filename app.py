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
            pass

        elif user_input == 'l':
            pass

        elif user_input == 'm':
            pass

        elif user_input == 'd':
            pass

        elif user_input == 'q':
            print("Programme terminated")
            break
        else:
            print("That choice doesn't exist, try again.")



# user input name and author of a book to add to database
# list all books in the database
# user input name to edit book status
# user input name to delete from database


menu()