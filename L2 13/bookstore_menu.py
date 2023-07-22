class Menu():
    # Got help from a friend here
    @staticmethod
    def select_options():
        options = "Select one of the following options below:\n"
        user_options = '''
        1 - Enter a book
        2 - Update book
        3 - Delete book
        4 - Search books
        5 - View all books
        0 - Exit
        '''
        print(options + user_options)
        return input("Enter your choice: ")
    
    # Got help from a friend here
    @staticmethod
    def menu_exit():
        print("Goodbye!!!")
        exit()