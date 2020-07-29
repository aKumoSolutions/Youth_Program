# def Name():
#     return "my first function"

# print(Name()

# names = ['abdul', 'adam']

# def append_name(list,value):
#     list.append(value)
#     print (list)

# append_name (names, 'saad')
# print (names)

# list of the students 

def stud(list, student):
    if student in list:
        print("student exists within this list")
    else:
        list.append(student)
        print(student + " has been added to list")
        print(list)

def rm_stud(list, student):
    if student in list:
        list.remove(student)
        print (student + "does not exist")
    else:
        print (student + "has been removed from the list")

students = ['abdul', 'umid', 'saad']

question = input("Would you like to add a student?: ")
# yesAswer =['yes', 'yeah']

if question == yes:
    student = input("enter the students name ")
    stud(students, student)

else:
    print("okay")


stud(students, 'adam')