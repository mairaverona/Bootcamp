import sqlite3

try:
    # Connect to the database or create it if it doesn't exist
    db = sqlite3.connect('python_programming.db')

    # Get a cursor object - you need this to be able to interact with the database
    cursor = db.cursor()

    # Create the table if it doesn't exist (exceptions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS python_programming (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade INTEGER
        )
    ''')

    # Inserting data into the table
    users_information = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]

    # Insert multiple rows into the table using executemany with INSERT OR REPLACE
    cursor.executemany('INSERT OR REPLACE INTO python_programming (id, name, grade) VALUES (?, ?, ?)', users_information)

    # Commit the changes to the database
    db.commit()

    # Select all grades between 60 and 80
    cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80''')
    # Fetch all the records
    records = cursor.fetchall()

    # Print the records
    print('Retrieved records (grades between 60 and 80):')
    for record in records:
        print(record)

    # Update student grade to 65
    grade = 65
    id1 = 55
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ?''', (grade, id1))
    db.commit()
    print('Updated student grade (ID: {}) to {}'.format(id1, grade))

    # Delete row
    id2 = 66
    cursor.execute('''DELETE FROM python_programming WHERE id = ?''', (id2,))
    db.commit()
    print('Deleted student with ID: {}'.format(id2))

    # Change the grade of all people with an ID below 55
    new_grade = 70
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < ?''', (new_grade, 55))
    db.commit()
    print('Changed grades below ID 55 to {}'.format(new_grade))

except sqlite3.Error as e:
    # Roll back any changes if something goes wrong
    db.rollback()
    print('An error occurred:', str(e))

finally:
    # Close the database connection
    db.close()
    print('Connection to database closed')








