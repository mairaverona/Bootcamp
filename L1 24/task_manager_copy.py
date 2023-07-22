import datetime
from pathlib import Path

def login_user_function():
    with open("user_copy.txt", "r") as users_file:
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
    #function needs to return
    return username

#main function that will call all the functions
#will contain the main while loop
#it is good practice to call the primary function the main function
def main():
    username = login_user_function()
    print(username)
    #function needs to return
    while True:
        main_menu = select_options(username)
        if main_menu == "r":
            reg_user(username)
        elif main_menu == "a":
            add_task()
        elif main_menu == "va":
            view_all()
        elif main_menu == "vm":
            view_mine(username)
        elif main_menu == "gr":
            generate_reports_tasks()
            generate_reports_users()
        elif main_menu == "ds":
            display_stat()
        elif main_menu == "e":
            menu_exit()
        else:
            print("You have made a wrong choice, please try again")

def select_options(username):
    options_title = "Select one of the following options below:\n"
    user_options = '''a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    '''
    admin_options = '''
    r - Registering a user
    gr - Generate reports
    ds - Display statistics
    '''

    if username == "admin":
        options = options_title + admin_options + user_options
    else:
        options = options_title + user_options
    
    #ask the user what they want to do 
    menu = input(options)
    #function needs to return
    return menu

def reg_user(username):
    if username == "admin":
    #while loop that continues until the user enters a unique username.
        while True:
            new_user = input("Enter your new username: ")
    #read the existing usernames from the user.txt file to check if the new username already exists
            with open("user_copy.txt", "r") as users_read:
                users_list = users_read.read().splitlines()
                existing_users = [user.split(',')[0] for user in users_list]
    #if the username already exists, we print an error message and prompt the user to enter a different username
                if new_user in existing_users:
                    print("This username already exists. Please enter a different username.")
                else:
                    new_password = input("Enter your new password: ")
                    password_confirmation = input("Confirm your password: ")
                    if new_password == password_confirmation:
                        with open("user_copy.txt", "a") as users_write:
                            users_write.write("\n" + new_user + ", " + new_password)
                            print("New user successfully registered")
                        break
                    else:
                        print("Your password is incorrect")

def add_task():
    user_name = input("Please enter the name of the user this task is assign to: ")
    task_title = input("Enter the tittle of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD) of this task: ")
    current_date = str(datetime.date.today())
    with open("tasks_copy.txt", "a") as tasks_write:
        tasks_write.write("\n" + user_name + ", " + task_title + ", " + description + ", " + due_date + ", " + current_date + ", " + "No")
        print("New task succesfully added")

def view_all():
    with open("tasks_copy.txt", "r") as easy_view:
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

def view_mine(username):
    with open("tasks_copy.txt", "r") as check_username:
        #initialize an empty list which will be used to store all the tasks assigned to the user
        tasks = []
        for line in check_username:
        #strip off any leading or white spaces
        #split the line into a list using the comma and space separator
            task = line.strip().split(", ")
            if task[0] == username:
        #if the first element matches the given username, appended to the tasks list
                tasks.append(task)
        if tasks:
        #print a heading and a numbered list of all the tasks assigned to the user
            print("Tasks assigned to you:")
        #enumerate() used to generate the index of each task, starting from 1
        #and then unpacks each task into its individual elements
            for i, task in enumerate(tasks):
                task_title, user_name, current_date, due_date, task_complete, description = task
                print(f"{i+1}. {task_title}")
            print("Enter task number to view or -1 to return to the main menu:")
        #loop prompts the user to select a task number to view the details of that task
        #if the user enters "-1", break the loop
            while True:
                choice = input(">> ")
                if choice == "-1":
                    break
        #check if the input is a valid integer between 1 and the number of tasks assigned to the user
                elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(tasks):
                    print("Invalid choice, please enter a valid task number or -1 to return to the main menu.")
        #if the input is valid, it selects the corresponding task from the tasks list
        #show it into its individual elements - print the details of the task
                else:
                    task = tasks[int(choice)-1]
                    task_title, user_name, current_date, due_date, task_complete, description = task
                    print(f'''
                    Task: {task_title}
                    Assigned to: {user_name}
                    Date assigned: {current_date}
                    Due date: {due_date}
                    Task Complete?: {task_complete}
                    Description: {description}
                    ''')
        #check whether the task that was selected by the user is incomplete
        #if incomplete, give the option to mark it as complete or edit it
                    if task_complete.lower() == "no":
                        print("Enter 'C' to mark task as complete, 'E' to edit task, or -1 to return to the main menu:")
                        while True:
                            sub_choice = input(">> ").lower()
                            if sub_choice == "-1":
                                break
                            elif sub_choice == "c":
                                task[4] = "Yes"
        #open the "tasks_copy.txt" file in write mode and write all the tasks
                                with open("tasks_copy.txt", "w") as tasks_file:
                                    for t in tasks:
                                        tasks_file.write(", ".join(t) + "\n")
                                print("Task marked as complete.")
                                break
        #give choice for user to edit the tasks - if incomplete (ask this)
                            elif sub_choice == "e":
                                if task_complete.lower() == "yes":
                                    print("Task has already been completed and cannot be edited.")
                                else:
                                    print("Enter 'U' to update assigned user or 'D' to update due date, or -1 to cancel:")
                                    while True:
                                        edit_choice = input(">> ").lower()
                                        if edit_choice == "-1":
                                            break
        #here the user asked to update assigned user, so ask for input on new assigned user
                                        elif edit_choice == "u":
                                            new_user = input("Enter new assigned user: ")
                                            task[1] = new_user
        #open tasks_copy in writing mode to be able to add new information to the file
                                            with open("tasks_copy.txt", "w") as tasks_file:
                                                for t in tasks:
                                                    tasks_file.write(", ".join(t) + "\n")
                                            print("Assigned user updated.")
                                            break
        #same as above but for new due date
                                        elif edit_choice == "d":
                                            new_date = input("Enter new due date (format: yyyy-mm-dd): ")
                                            task[3] = new_date
                                            with open("tasks_copy.txt", "w") as tasks_file:
                                                for t in tasks:
                                                    tasks_file.write(", ".join(t) + "\n")
                                            print("Due date updated.")
                                            break
        #is there a more efficient way here?
                                        else:
                                            print("Invalid choice, please enter 'U' or 'D' or -1 to cancel.")
                            else:
                                print("Invalid choice, please enter 'C' or 'E' or -1 to return to the main menu.")
                    else:
                        print("This task has already been marked as complete and cannot be edited.")
        else:
            print("No tasks assigned to you.")

def generate_reports_tasks():
    total_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0
    #opening file in read mode
    with open("tasks_copy.txt", "r") as total_tasks_file:
        for line in total_tasks_file:
            _, _, _, due_date, _, task_complete = line.strip().split(", ")
            total_tasks += 1
            due_date_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    #get total number of completed tasks
            if task_complete == "yes":
                completed_tasks += 1
    #get total number of tasks that are overdue
            elif due_date_object < datetime.date.today():
                overdue_tasks += 1
  
    #get total number of uncompleted tasks
    uncompleted_tasks = total_tasks - completed_tasks
    #get percentage of tasks that are incomplete
    percent_incomplete = (uncompleted_tasks / total_tasks) * 100
    #get percentage of tasks that are overdue
    percent_overdue = (overdue_tasks / total_tasks) * 100

    #generate task overview report
    with open('task_overview.txt', 'w') as f:
        f.write(f'Total number of tasks: {total_tasks}\n')
        f.write(f'Total number of completed tasks: {completed_tasks}\n')
        f.write(f'Total number of uncompleted tasks: {uncompleted_tasks}\n')
        f.write(f'Total number of tasks that are overdue: {overdue_tasks}\n')
        f.write(f'Percentage of tasks that are incomplete: {percent_incomplete:.2f}%\n')
        f.write(f'Percentage of tasks that are overdue: {percent_overdue:.2f}%\n')

def generate_reports_users():
    #get total number of users registered
    total_users = 0
    usernames = []
    with open("user_copy.txt", "r") as total_users_file:
        for line in total_users_file:
            user, _ = line.strip().split(", ")
            usernames.append(user)
            total_users += 1
    
    total_tasks = 0
    tasks_list = []
    with open("tasks_copy.txt", "r") as total_tasks_file:
        for line in total_tasks_file:
            tasks_list.append(line)
            total_tasks += 1

    with open('user_overview.txt', 'w') as users_taks:
        users_taks.write(f'Total users: {total_users}\n')
        users_taks.write(f'Total tasks: {total_tasks}\n\n')
        for user in usernames:
            total_tasks_per_user = 0
            total_complete_tasks = 0
            total_overdue_tasks = 0
            for task in tasks_list:
                user_name, _, _, due_date, _, task_complete = task.strip().split(", ")
                if user_name == user:
                    total_tasks_per_user += 1
                    due_date_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                    if task_complete == "yes":
                        total_complete_tasks +=1
                    elif due_date_object < datetime.date.today():
                        total_overdue_tasks +=1
        
            percent_assigned = (total_tasks_per_user / total_tasks) * 100
            percent_completed = (total_complete_tasks / total_tasks_per_user) * 100
            total_uncomplete_tasks = total_tasks_per_user - total_complete_tasks
            percent_uncompleted = (total_uncomplete_tasks / total_tasks_per_user) * 100
            percent_overdue = (total_overdue_tasks / total_tasks_per_user) * 100
            users_taks.write(f'{user}\n')
            users_taks.write(f'Total number of tasks assigned: {total_tasks_per_user}\n')
            users_taks.write(f'Percentage of tasks assigned: {percent_assigned:.2f}%\n')
            users_taks.write(f'Percentage of tasks completed: {percent_completed:.2f}%\n')
            users_taks.write(f'Percentage of tasks uncompleted: {percent_uncompleted:.2f}%\n')
            users_taks.write(f'Percentage of tasks overdue: {percent_overdue:.2f}%\n\n')

def display_stat():
    #how to check if a file exists and create one if not
    if not Path("task_overview.txt").exists():
        generate_reports_tasks()

    if not Path("user_overview.txt").exists():
        generate_reports_users()

    task_overview = open("task_overview.txt", "r").read()
    user_overview = open("user_overview.txt", "r").read()
    
    print(task_overview)
    print("\n")
    print(user_overview)
    
def menu_exit():
    print('Goodbye!!!')
    exit()

main()