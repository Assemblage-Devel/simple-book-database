"""
a Books database app with menu
"""

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




menu()