class person:
    pass

# Define a Car class with a class attribute 'hp'
class Car:
    hp = 450  # Class attribute shared by all Car objects
# Create an instance of the Car class
car1 = Car()
# Print the horsepower value from the object
print(car1.hp)  # Output: 450

# Define a Car class with a constructor (__init__) that takes horsepower as a parameter
class Car:
    def __init__(self, hp, model, brand, year):
        self.horsepower = hp  # Instance attribute unique to each Car object
        self.model = model
        self.brand = brand
        self.year = year
    def info(self):
        return f"{self.horsepower} {self.brand} {self.model} {self.year}"
# Create an instance of the Car class and pass the horsepower value
car1 = Car(612, "CarreraGT", "Porsche", 2003)
car2 = Car(500, "Gallardo", "Lamborghini", 2003)
car1.horsepower = 612
# del car1.horsepower ----> AttributeError: 'Car' object has no attribute 'horsepower'


# Print the horsepower stored in the instance attribute
print(car1.info())
print(car2.info())
print(car1.horsepower)

