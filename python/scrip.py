# names = ['Abdul', 'Adam']

# def append_name(list, value):
#     list.append(value)
#     print(list)

# append_name(names, 'Saad')

# List of the student

def stud(list, student):
    if student in list:
        print("Student Exists within this list")
    else:
        list.append(student)
        print(student + " Has been added to list")
        print(list)

def rm_stud(list, student):
    if student in list:
        list.remove(student)
        print(student + " has been removed from the list")
        print(list)
    else:
        print(student + " does not exist")
        print(list)


students = ['Abdul', 'Umid', 'Saad']

question = input("Would you like to add a student? [add, remove, nothing]: ")
yesAswer = ['yes', 'yea', 'yo', 'yeah', 'YEA', 'YES', 'add', 'ad']

# if question == 'add':
if question in yesAswer:
    student = input("Enter the student's name? ")
    stud(students, student)

elif question == 'remove':
    student = input("Enter the student's name? ")
    rm_stud(students, student)
else:
    print("Okay")

