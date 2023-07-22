class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):          #innitialiser function
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):                                             #overrid function in case can't drive
        print(f"{self.name} is too young to drive.")

name = input("What is your name: ")                                  #take inputs
age = int(input("How old are you: "))
hair_colour = input("What is your hair colour: ")
eye_colour = input("What is the colour of your eyes: ")
    
if age >= 18: #if function to check if the person is old enough to drive
    person = Adult(name, age, hair_colour, eye_colour)  #instance of the Adult class
else:
    person = Child(name, age, hair_colour, eye_colour)  #instance of the Child class

person.can_drive()
