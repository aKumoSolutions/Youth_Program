


def add_dict(name, age, email,):
    gender = input ('Enter the gender of the students')
    name = input("Enter the name of the students")
    age = input("Enter the age of the student")
    email = input("Enter the email of the student")
    age = int(age)
    data ['students'].append({ 
        'name' : name,
        'age' : age,
        'email' : email,
    }) 
print('Student' + name + 'has been added into students list in data dict')


def gender_dict()
    if gender in Male:
        name = input("Enter the name of the students")
        age = input("Enter the age of the student")
        email = input("Enter the email of the student")
        age = int(age)
        data['Male'].append({
            'name' : name,
            'age' : age,
            'email' : email,
        })
        with open('SaadM.txt', 'w') as outfile:
    json.dump(data['Male'], outfile)

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
       
with open('SaadF.txt', 'w') as outfile:
    json.dump(data['Female'], outfile)
       
        print('Female Idividual has been added')
    else: 
        print('There are only 2 genders')


data = {}
data ['Male'] = []
data ['Female'] = [] 
gender_dict()




