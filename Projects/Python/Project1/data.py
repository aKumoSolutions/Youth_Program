import json

gender = input("Please enter your gender(F, M): ")
Male = ['M', 'm', 'male', 'boy', 'man']
Female = ['F', 'f', 'female', 'girl', 'woman']

#creating function
def add_dict(name, age, email):
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    email = input("Enter the email of the student: ")
    age = int(age)
    data['students'].append({
        'name': name,
        'age': age,
        'email': email
    })
    print('Student' + name + 'has been added into students list in Data dict')

def gender_dict():
    if gender in Male:
        name = input("Enter the name of the student: ")
        age = input("Enter the age of the student: ")
        email = input("Enter the email of the student: ")
        age = int(age)
        data['Male'].append({
            'name': name,
            'age': age,
            'email': email
        })
        with open('AbdulM.txt', 'w') as outfile:
            json.dump(data['Male'], outfile)
        print('Male indivitual has been added')
        print(data['Male'])

    elif gender in Female:
        name = input("Enter the name of the student: ")
        age = input("Enter the age of the student: ")
        email = input("Enter the email of the student: ")
        age = int(age)
        data['Female'].append({
            'name': name,
            'age': age,
            'email': email
        })
        with open('AbdulM.txt', 'w') as outfile:
            json.dump(data['Male'], outfile)
        print('Female individual has been added')
        print(data['Female'])
    else: 
        print('There are only 2 genders, biologically speaking.')


#creating dictionary called 'data'
data = {}
data['Male'] = []
data['Female'] = []
gender_dict()