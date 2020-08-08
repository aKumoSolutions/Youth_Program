import json

gender = input("Please enter your gender(F, M): ")
name = input("Enter the name of the student: ")
age = input("Enter the age of the student: ")
email = input("Enter the email of the student: ")
age = int(age)
Male = ['M', 'm', 'dude', 'guy', 'boy', 'male']
Female = ['F', 'f', 'girl', 'female', 'woman']


# #creating function
# def add_dict(name, age, email):
#     data['students'].append({
#         'name': name,
#         'age': age,
#         'email': email
#     })
#     print('Student' + name + 'has been added into students list in Data dict')

def gender_dict(name, age, email):
    if gender in Male:
        data['Male'].append({
            'name': name,
            'age': age,
            'email': email,
        })
        with open('UmidM.txt')
        print('Male individual has been added')  
    elif gender in Female:
        data['Female'].append({
            'name': name,
            'age': age,
            'email': email
        })
        
        print('Female individual has been added')
    else:
        ('There are only 2 gender, biologically speaking.')      

#creating dictionary called 'data'
data = {}
data['Male'] = []
data['Female'] = []

gender_dict(name, age, email)


add_dict(name, age, email)

print(data)
