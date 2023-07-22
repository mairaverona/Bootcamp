from bookstore_menu import Menu
from bookstore_database import Database

def main():
    menu = Menu()
    database = Database()
    database.create_database()
    while True:
        option = menu.select_options()
        if option == "1":
            database.add_new_books()
        elif option == "2":
            database.update_table()
        elif option == "3":
            database.delete_from_table()
        elif option == "4":
            database.search_database()
        elif option == "5":
            database.view_all_books()
        elif option == "0":
            menu.menu_exit()
            database.close_database()
        else:
            print("You have made a wrong choice, please try again")

main()