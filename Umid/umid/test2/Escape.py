

# students = ['Abdul', 'Umid', 'Saad']names = ['Abdul', 'Adam']

# def append_name(list, value):
#     list.append(value)
#     print(list)

# append_name(names, 'Saad')
def stud(list, student):
    if student in list:
        print("Student exists within this list")
    else: 
        list.append(student)
        print(student + " has been added to list")
        print(list) 

students = ['Abdul', 'Umid', 'Saad']
question = input("Would you like to add a student?: ")
# yesAnswer = ['yes', 'ye', 'y', 'YES', 'yeah']
if question == 'yes':
    student = input("Enter the student's name: ")
    stud(students, student)
else: 
    print("Okay")


