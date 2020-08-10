# class Person:
#     def__init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

class Car:
    def __init__(self):
         self.displacement = input("Enter your engine displacement: ")
         self.cylinders = input("Enter number of cylinders: ")

car1 = Car()

print(car1.displacement + ' ' + car1.cylinders)
