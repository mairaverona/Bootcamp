#=====importing libraries===========
'''This is the section where you will import libraries'''

import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
with open("user.txt", "r") as users_file:
    users = {}
    for line in users_file:
        username, password = line.strip().split(", ")
        users[username] = password
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username not in users:
        print("This user does not exist")
    elif password != users[username]:
        print("Incorrect password")
    else:
        print("Login successful!")
        break

while True:
    options_title = "Select one of the following Options below:\n"
    
    user_options = '''a - Adding a task
va - View all tasks
vm - view my task
e - Exit
'''
    admin_options = '''r - Registering a user
s - Statistics'''

    if username == "admin":
        options = options_title + admin_options + user_options
    else:
        options = options_title + user_options
        
    menu = input(options)

    if menu == 'r':
        if username == "admin":
            new_user = input("Enter your new username: ")
            new_password = input("Enter your new password: ")
            password_confirmation = input("Confirm your password: ")
            if new_password == password_confirmation:
                with open("user.txt", "a") as users_write:
                    users_write.write("\n" + new_user + ", " + new_password)
                    print("New user succesfully registered")        
            else:
                print("Your password is incorrect")
        else:
            print("You don't have access to this option")

    elif menu == 'a':
        user_name = input("Please enter the name of the user this task is assign to: ")
        task_title = input("Enter the tittle of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of this task: ")
        current_date = str(datetime.date.today())
        with open("tasks.txt", "a") as tasks_write:
            tasks_write.write("\n" + user_name + ", " + task_title + ", " + description + ", " + due_date + ", " + current_date + ", " + "No")
            print("New task succesfully added")

    elif menu == 'va':
        with open("tasks.txt", "r") as easy_view:
            for line in easy_view:
                user_name, task_title, description, due_date, current_date, task_complete = line.strip().split(", ")
                output2 = '''
                Task: {}
                Assigned to: {}
                Date assigned: {}
                Due date: {}
                Task Complete?: {}
                Description: {}
                '''.format(task_title, user_name, current_date, due_date, task_complete, description)
                print(output2)

    elif menu == 'vm':
        with open("tasks.txt", "r") as check_username:
            for line in check_username:
                user_name, task_title, description, due_date, current_date, task_complete = line.strip().split(", ")
                if user_name == username:
                    output2 = '''
                    Task: {}
                    Assigned to: {}
                    Date assigned: {}
                    Due date: {}
                    Task Complete?: {}
                    Description: {}
                    '''.format(task_title, user_name, current_date, due_date, task_complete, description)
                    print(output2)

    elif menu == "s":
        total_task = 0
        total_user = 0
        with open("tasks.txt", "r") as total_tasks:
            for line in total_tasks:
                total_task += 1
        with open("user.txt", "r") as total_users:
            for line in total_users:
                total_user += 1
            output0 = '''
        Total tasks = {}
        Total users = {}
        '''.format(total_task, total_user)
            print(output0)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again")