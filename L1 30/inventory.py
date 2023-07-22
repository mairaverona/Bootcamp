from tabulate import tabulate


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #accessesing the cost attribute of the Shoe instance to return (return) its value
    def get_cost(self):
        return self.cost

    #accessesing the quantity attribute of the Shoe instance to returns (return) its value
    def get_quantity(self):
        return self.quantity

    #creating a string using the values of the above atributes
    def __str__(self):
        return f"Shoe({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})"

#empty shoe list that will be appended in the functions to follow
shoe_list = []


def main():
    #creating the while loop to make sure the menu is diplayed repeatedly 
    #using all options possible and and exit one
    while True:
        print("=== Shoe Inventory Management ===")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Search Shoe")
        print("4. Value per Item")
        print("5. Re-Stock")
        print("6. Show Shoe with Highest Quantity")
        print("7. Exit")

        #asking input on which option user wants to choose
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            #asking input on shoe code, so it shows the correct one
            code = input("Enter the shoe code: ")
            shoe = search_shoe(code)
            if shoe:
                print("Shoe found:")
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == "4":
            value_per_item()
        elif choice == "5":
            re_stock()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        #printing an empty line for better readability
        print()


def read_shoes_data(code=None):
    #using try at the beginning for error catching later
    try:
        #opening the file in read mode as file
        with open("inventory.txt", "r") as file:
            #skipping the first line
            next(file)

            for line in file:
                #removing leading/trailing whitespace
                line = line.strip()
                #splitting the lines into separated data elements
                data = line.split(",")
                if len(data) >= 5:
                    #extracting the data to be able to create a shoe object
                    country = data[0]
                    code = data[1]
                    product = data[2]
                    cost = float(data[3])
                    quantity = int(data[4])
                    #creating a new Shoe object
                    shoe = Shoe(country, code, product, cost, quantity)
                    #appending the data to the empty list
                    shoe_list.append(shoe)
    except FileNotFoundError:
        #exception handling - first to check if the file exists
        #then a more general exception to catch other errors that might appear
        print("File 'inventory.txt' not found.")
    except Exception as e:
        print("Error occurred while reading the file:", str(e))


def capture_shoes():
    #using it again for error handling at the end
    try:
        #getting input on all the elements
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        #creating a new Shoe object - creates a new instance of the Shoe class, 
        #and you can use it in multiple functions as needed - making a note on why I used this twice
        shoe = Shoe(country, code, product, cost, quantity)
         #appending the data to list
        shoe_list.append(shoe)
    except ValueError:
        #this exception is raised when there is an error converting input 
        #for cost or quantity to a float or int.
        print("Invalid input for cost or quantity.")
    except Exception as e:
        print("Error occurred:", str(e))


def view_all():
    #checking if show list is not empty
    if shoe_list:
        #creating a list to hold the table data
        table_data = []

        for shoe in shoe_list:
            #getting the details of the shoe using the __str__() method
            shoe_details = str(shoe).split(", ")
            #appending the details as a row to the table_data list
            table_data.append(shoe_details)
        #specifying the table headers
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        #printing using the tabulate module
        print(tabulate(table_data, headers, tablefmt="grid"))
    else:
        print("No shoes found in the list.")


def re_stock():
    if shoe_list:
        #the lambda function acts as a key function, allowing min() to determine the minimum based on the quantity
        #x represents each Shoe object during iteration, and x.get_quantity() retrieves the quantity attribute of that object
        min_quantity_shoe = min(shoe_list, key=lambda x: x.get_quantity())
        print("Lowest quantity shoe:")
        print(min_quantity_shoe)

        try:
            #asking user input to add more shoes
            add_quantity = int(input("Enter the quantity to add: "))
            #updating the quantity in the shoe object
            min_quantity_shoe.quantity += add_quantity
            #updating the quantity in the file
            update_file_quantity(min_quantity_shoe)
            print("Quantity updated successfully.")
        except ValueError:
            print("Invalid input for quantity.")
        except Exception as e:
            print("Error occurred:", str(e))
    else:
        print("No shoes found in the list.")

#created a new function to update quantity for better code reusability
#and also to make it more modular and easier to mantain
def update_file_quantity(shoe):
    try:
        #reading the lines from the file
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        #updating quantity in the appropriate line 
        for i, line in enumerate(lines):
            data = line.strip().split(",")
            file_code = data[1]
            if file_code == shoe.code:
                data[4] = str(shoe.quantity)
                lines[i] = ",".join(data) + "\n"
                break
        #updating the lines on the file
        with open("inventory.txt", "w") as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("File 'inventory.txt' not found.")
    except Exception as e:
        print("Error occurred while updating the file:", str(e))


def search_shoe(code):
    #checking if the code matches, if it does return the code if not return None
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None

#performing calculating as per exercise on how to get the total value
#then printing it using f
def value_per_item():
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"Shoe Code: {shoe.code}, Total Value: {total_value}")


def highest_qty():
    if shoe_list:
        #using lambda function again so it understands "quantity" as comparison value
        max_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
        print("The shoe with the highest quantity is for sale:")
        print(max_quantity_shoe)
    else:
        print("No shoes found in the list.")


#here I am ensuring the code inside this block will only be executed when the script is run as the main program
#it prevents the code from executing if the script is imported as a module
if __name__ == "__main__":
    read_shoes_data()
    main()