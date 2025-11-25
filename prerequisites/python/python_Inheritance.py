class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob 
    def __str__ (self):
        return f"{self.name} Person Object"
person0 = Person("Jennifer"," December 12, 1970")
print(person0)