import json

#creating function
def add_dict(name, age, email):
    name = input("enter the name of the student: ")
    age = input("enter the age of the student: ")
    email = input("enter the email of the student: ")
    data['students'].append({
        'name': name,
        'age': age,
        'email': email

    })
    print('student' + name + 'has been added into students list in data dict')
        


def gender_dict(name, age, email):
    if gender == 'M':
        data['male'].append({
            'name' : name,
            'age' : age,
            'email': email,
        })
        print ('male individual has been added')
    elif gender == 'F'
        data['Female'].append({
         'name' : name,
         'age' : age,
         'email' : email
         print('Female individual has been added')
    else:
         print:(there are only 2 genders, biologically speaking.')

#creating dictionary called 'data'
data = {}
data['male'] = []
data['female'] = []
    
