# class UmidClass:
#     x = 5

# pi = UmidClass()
# print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

class Car: 
    def __init__(self):
        self.displacment = input("Enter your engine displacement: ")
        self.cylinders = input("Enter number of cylinders: ")
car1 = Car()

print("Your car is " + car1.displacment + "L and it has " + car1.cylinders + " cylinders")

print(car1.cylinders)

