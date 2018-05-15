import random 
number = random.randint(0,3)

words = ["STEELERS", "JAZZ", "CLAY"]

hint1 = ["Football", "Basketball", "Athlete"]

hint2 = ["Pittsburgh", "Donivan Mitchell", "Gamer"]

guess = ""

counter = 1

secretword = words [number]

while True:
    print ("Guess the secret word!")
    print ("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input() .upper()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "HINT1":
        print (hint1 [number] )

    elif guess == "HINT2":
        print (hint2 [number] )

    elif guess == "FIRST LETTER":
        print (secretword [0] )

    elif guess == "LAST LETTER":
        print ("The secret word was " + secretword)

    else:
        print("Try Again!")
        counter += 1


