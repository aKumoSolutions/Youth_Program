

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

class Car:
    def __init__(self, displacement, cylinders):
        self.displacement = displacement
        self.cylinders = cylinders
car1 = Car("5L", "V8")
car2 = Car("2L", "i3")

print(car2.cylinders)
