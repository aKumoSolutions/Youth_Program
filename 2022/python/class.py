class Student:
    'A student class'
    stuCount = 0
  
    # initialization or constructor method of
    def __init__(self):  
          
        # class Student
        self.name = input('enter student name:')
        self.rollno = input('enter student rollno:')
        Student.stuCount += 1
  
    # displayStudent method of class Student
    def displayStudent(self):  
        print("Name:", self.name, "Rollno:", self.rollno)