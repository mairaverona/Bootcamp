class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"
   
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
        
    def head_office_location(self):
        print("Our head office is located in ", self.head_office_location)

class OOPCourse(Course):
    description = "Learn everything you need to create amazing computer programs."
    trainer = "Mr Anon A. Mouse"

    def __innit__(self):               #innitialiser function
        self.description
        self.trainer

    def trainer_details(self):
        print("Course description: ", self.description)
        print("Trainer: ", self.trainer)

    def show_course_id(self):
        print("Course ID:: #12345")

#actions: create an object of subclass
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

            


    
