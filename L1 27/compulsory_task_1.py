import os          #to be able to check if the file we are trying to open exists

#create a function with all the calculations we want to perform, will be called later on the while loop
def operation(num_1, num_2, operation_input):
    if operation_input == "+":
            result = num_1 + num_2
    elif operation_input == "-":
            result = num_1 - num_2
    elif operation_input == "*":
            result = num_1 * num_2
    elif operation_input == "/":
            result = num_1 / num_2
    elif operation_input == "%":
            result = num_1 % num_2
    elif operation_input == "**":
            result = num_1 ** num_2
    elif operation_input == "//":
            result = num_1 // num_2
    else:
        raise ValueError("Invalid operation!")
    
    print("The result is:", result)

    #open the file to write the calculations to
    with open("equations.txt", "a") as file:
        equation = f"{num_1} {operation_input} {num_2} = {result}\n"
        file.write(equation)

#use a while loop to ask the user for input and then use if to add value to the option chosen by the user
while True:
    user_choice = input("Please select option 1 to perform calculations or option 2 to read calculations file: ")

    if user_choice == "1":
        try:
            num_1 = float(input("Please input your first number: "))
            num_2 = float(input("Please input your second number: "))
            operation_input = input("Please input the operation to be performed (e.g. +, -, x, etc.): ")
            #calling the function here to perform the calculations
            operation(num_1, num_2, operation_input)
        #used open "as e" because this way you can assign the caught exception object to the variable e
        except ValueError as e:
            print("Error:", str(e))
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
    
    elif user_choice == "2":
        file_does_not_exist = True    #this is to able to break out of the loop
        while file_does_not_exist:  
            try:
                file_name = input("Please enter the name of the file: ")
                if os.path.exists(f"{file_name}.txt"):            #here is where the "import os" comes
                    with open(f"{file_name}.txt", "r") as file:
                        calculations = file.read()
                        print("Calculations from file:\n")
                        print(calculations)
                    file_does_not_exist = False          #if they write the correct name, the file shows and the loop ends
            except FileNotFoundError as error:
                print(error)
    else:
        print("Invalid choice. Please try again.")