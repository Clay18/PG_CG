import random
import time

number = random.randint (1, 100)

guess = 0

counter = 0

while True:
    print ("Guess my number between 1 and 100!")
    guess = int (input())
    counter += 1

    if guess == number:
        print ("You got it!!!")


    elif guess > number:
        print ("Too high bud! Try again.")

    elif guess < number:
        print ("Too Low my son! Try again.")
        

