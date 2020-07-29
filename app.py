print("Welcome to my first Game !!!")
name = input('What is your name? ')
age = int(input('What is your age? '))
print(f'"Hello", {name}, "you are", {age}, years old.')

'''Condition for age'''
if age >= 14:
    print("You are old enough!")

    wants_to_play = input('Do you want to play? ')
    if wants_to_play == "yes":
        print("Let's play !!!")













else:
    print("You are not old enough to play this game... ")

