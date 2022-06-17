class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

p1 = Person("John", 36)


class Car:
    def __init__(self):
        self.displacement = input("Enter the car displacement NOW: ")
        self.cylinder = input("Enter the car cylinder NOW: ")
car1 = Car()

print("Your car is" + car1.displacement + "L and it has " + car1.cylinder + "cylinder")




