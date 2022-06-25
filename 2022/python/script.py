#!/usr/bin/env python3

members = [
    {"id": "01", "name": "Justin", "title": "student", "age": 20}, 
    {"id": "02", "name": "Uruj", "title": "student", "age": 13}
]

name = input("Hello there 👋, whats your name?: ")

if name == members[1]['name'] and members[1]['age'] <= 18:

	print("Youre one of our young members")

	print("Welcome to aKumoSolutions, %s" % name)

else:
	print("You arent enrolled %s" % name)

