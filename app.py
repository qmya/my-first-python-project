print("Welcome to my first Game !!!")
name = input('What is your name? ')
age = int(input('What is your age? '))
print(f'"Hello", {name}, "you are", {age}, years old.')

'''Condition for age'''
health = 10
print(f"You are starting with {health} health")
if age >= 14:
    print("You are old enough!")

    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print("Let's play !!!")
        left_or_right = input('First choice... Left or Right (Left/Right)?  ').lower()
        if left_or_right == "right":
            ans = input("Nice, you follow the path and reach a lake.Do you swim across or go around (across/around)? ").lower()
            if ans == "around":
                print("You went around and reach the other side of the lake")
            elif ans == "across":
                print("You managed to get across , but were bit by a fish and lost five health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":

            else:
                print('You lose')
        else:
            print('You lost....')
    else:
        print('Bye....')













else:
    print("You are not old enough to play this game... ")

