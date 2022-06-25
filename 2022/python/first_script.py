import sys

students = ["Abdul", "Justin", "Uruj"]
name = input("Please enter name: ")

for student in students:
    if student == name:
        print("Student " + name + " is enrolled")
        sys.exit()

print("Student " + name + " not enrolled")