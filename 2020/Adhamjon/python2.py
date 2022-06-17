# name = ['Abdul', 'Adhamjon']

# def names(list, value):
#     list.append(value)
#     print(list)

# names(name,'Saad')

students = ['Abul', 'Umid', 'Saad']

def stud(list, student):
    if student in list:
        print("Student Exits")
    else:
        
        print("The " + student + " doesn't exit but has been added")
        list.append(student)

stud(students, 'Adhamjon')