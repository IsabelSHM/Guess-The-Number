#PRACTICE THIS ONE! this is with a library that i don't know, all the dificult things ill put on a list

import random
def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess again, Too low")
        elif guess > random_number:
            print("Sorry guess again, Too high")


    print(f"Congrats! You have guessed the number {random_number}!")

guess (10)

