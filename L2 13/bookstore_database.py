import sqlite3

class Database():
    # Connect to the database or create it if it doesn't exist
    db = sqlite3.connect('ebookstore.db')

    def create_database(self):
        try:
            # Get a cursor object - you need this to be able to interact with the database
            cursor = self.db.cursor()

            # Create the table if it doesn't exist (exceptions)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    qty INTEGER
                )
            ''')

            # Inserting data into the table
            books_list = [
                (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                (3002, 'Harry Potter and the Philosophers Stone', 'J.K.Rowling', 40),
                (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
                (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
                (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
            ]

            # Insert multiple rows into the table using executemany with INSERT OR REPLACE
            cursor.executemany('INSERT OR REPLACE INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)', books_list)

            # Commit the changes to the database
            self.db.commit()
            
        except Exception as e:
            print(e)
            self.close_database()

    # Add new books to the database
    def add_new_books(self):
        while True:
            try:
                new_book_id = int(input("Please input the book ID: "))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        new_book_title = input("Please input the book title: ")
        new_book_author = input("Please input the author of the book: ")
        while True:
                try:
                    new_book_qty = int(input("Please input quantity: "))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        self.db.cursor().execute('INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)', (new_book_id, new_book_title, new_book_author, new_book_qty))
        self.db.commit()
        print("New book added successfully")
    
    # Update table
    def update_table(self):
        while True:
            try:
                id = int(input("Which book id would you like to update? "))
                break
            except ValueError:
                print("Oops!  That was no valid id.  Try again...")
        new_title = input("Please input the new title: ")
        new_author = input("Please input new author: ")
        self.db.cursor().execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (new_title, new_author, id))
        self.db.commit()

    # Delete from table
    def delete_from_table(self):
        while True:
            try:
                id = int(input("What book id would you like to delete? "))
                break
            except ValueError:
                print("Oops!  That was no valid id.  Try again...")
        self.db.cursor().execute('DELETE FROM books WHERE id = ?', (id,))
        self.db.commit()
        print("Book deleted successfully")

    # Search database to find a specific book
    def search_database(self):
        search_title = input("Enter the title of the book you are looking for: ")
        cursor = self.db.cursor()  # Create a new cursor object
        cursor.execute('SELECT * FROM books WHERE title = ?', (search_title,))
        records = cursor.fetchone()  # Use cursor to fetch the records

    # Check if a record was found
        if records is not None:
            print("Book found: ")
            print(records)
        else:
            print("No book found with the title: ", search_title)

    # View all books in the database
    def view_all_books(self):
        cursor = self.db.cursor()  # Create a cursor object
        cursor.execute('SELECT * FROM books')
        records = cursor.fetchall()

        if records:
            print("All books in the database: ")
            for record in records:
                print(record)
        else:
            print("No books found in the database.")

    def close_database(self):
        self.db.close()
        print("Connection closed")














