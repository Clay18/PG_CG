import random 
number = random.randint(0,3)

words = ["Steelers", "Jazz", "Clay"]

hint 1 = ["Football", "Basketball", "Athlete"]

hint 2 = ["Pittsburgh", "Donivan Mitchell", "Gamer"]

guess = ""

counter = 1

secretword = words [number]

while True:
    print ("Guess the secret word!")
    print ("Type 'hint 1', 'hint 2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input()

    if guess == secret word:
        print("You win!")
        print("It took you " + str(counter + " guesses.")
        break

    
