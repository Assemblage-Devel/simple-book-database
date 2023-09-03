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
    user_choice = ' '
    while user_choice != 'q':
        user_choice = input(USER_CHOICE)
        
        if user_choice == 'a':
            pass

        elif user_choice == 'l':
            pass

        elif user_choice == 'm':
            pass

        elif user_choice == 'd':
            pass

        elif user_choice == 'q':
            print("Programme terminated")
            break
        else:
            print("That choice doesn't exist, try again.")



# user input name and author of a book to add to database
# list all books in the database
# user input name to edit book status
# user input name to delete from database


menu()