

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

class Car:
    def __init__(self):
        self.displacement = input("Enter your engine Displacement: ")
        self.cylinders = input("Enter number of cylinders: ")
car1 = Car()

print("Your car is " + car1.displacement + "L and it has " + car1.cylinders + " cycliders")
print(car1.displacement)