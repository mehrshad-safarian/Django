# Parent class Person
class Person:
    def __init__(self, name, dob):
        # Store name and date of birth
        self.name = name
        self.dob = dob
    def __str__(self):
        # String representation of Person
        return f"{self.name} Person Object"
# Child class Student inherits from Person
class Student(Person):
    def __init__(self, name, dob, grade):
        # Call parent constructor correctly
        super().__init__(name, dob)
        # Convert grade to integer for comparison
        self.grade = grade
    def __str__(self):
        # String representation of Student
        return f"{self.name} Student Object"
    def is__passing(self):
        # Return True if grade > 3, otherwise False
        return True if self.grade > 3 else False
# Create a student object
student1 = Student("Jennifer", "December 12, 1970", 100)
# Print object data
print(student1.name, student1.dob, student1.grade)
# Check if student is passing
print(student1.is__passing())



# Person creates a basic human with name and dob.
# Student is a special Person that also has a grade.
# super().__init__() is how Student borrows Person's variables.
# is__passing() checks if the grade is high enough.