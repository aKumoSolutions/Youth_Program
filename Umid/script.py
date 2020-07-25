# num= input("Please enter a number: ")
# num = int(num)

# if num % 2 == 0:
#     print("Your number is even!")
# else:
#     print:("Your number is odd.")

# elif = else if
# four = 2 + 2
# ten = 5 + 5
# three = 2 + 3

# if four != ten and three != four and bool(three) != False:
#     print("These are all unequal")
# elif bool(three) == True:
#     print(three + " is True!")
# else:
#     print("Any other condition")

name = input("Who are you?: ")

age = input("How old are you?: ")
age = int(age)


if age > 18:    
    print("Welcome to the party!")
else:
    print("Looks like we got a young gun on our hands.")

pizza = input("Did you bring pizza?: ")
# pizza = int(pizza)
maybeAnswer = ['maybe', 'Maybe', 'mybe', 'maybe', 'okay']
yesAnswer = ['yesh', 'ye', 'y', 'Y', 'yeah', 'yes', 'Yes']
noAnswer = ['NO', 'n', 'no', 'N', 'n0', 'nah', 'nope', 'not']

if pizza == yesAnswer:
    print("We're delighted to have you!")


elif pizza == noAnswer:
    print("I'm sure we'll find a use for you eventually.")


elif pizza == maybeAnswer:
    print("You seem unreliable...who are you really?")

else: 
    print("We're taking you to into the basement")