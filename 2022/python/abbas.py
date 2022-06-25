#!/usr/bin/env python3

members = [ 
        {"id": "01", "name" : "Justin", "title": "student", "age": 20},
        {"id": "02", "name" : "Abbas", "title": "student", "age": 16},
        {"id": "03", "name" : "Uruj", "title": "student", "age": 12}
]
        
name = input("Hello there, what's your name?: ")

if name == members[1]['name'] and members[1]['age'] < 18:
    print("You're one of our young members")
    print("Nice to meet you %s" % name)

elif name == members[0]['name'] and members[0]['age'] > 18:
        print("You're older than 18")
        print("Nice to meet you %s" % name)

elif name == members[2]['name'] and members[2]['age'] < 18:
    print("You're one of our young members")
    print("Nice to meet you %s" % name)
    
else:
    print("You aren't enrolled %s" % name)