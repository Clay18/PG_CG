import pyautogui as pg
import time
import webbrowser



#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) Sleep in a tub of earthworms.

b) Sleep in a tub of cockroches.


"""
    )
pg.alert ("You chose " + answer)

#Answers go here





#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) Eat 2 slugs.

b) Eat a cows eyeball.


"""
    )
pg.alert ("You chose " + answer)

#Answers go here




#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) Super Speed.

b) Super Strength.


"""
    )
pg.alert ("You chose " + answer)

#Answers go here



#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) In a cartoon.

b) A movie wuth your favorite actor.


"""
    )
pg.alert ("You chose " + answer)

#Answers go here



#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) live in the wilderness far from civilization.

b) live on the streets of a city as a homeless person.


"""
    )
pg.alert ("You chose " + answer)

#Answers go here


#Questions goes here
answer = pg.prompt(
"""
Would You Rather?

a) Go to jail for 4 years for something you didn’t do.

b) Get away with something horrible you did but always live in fear of being caught.


"""
    )
pg.alert ("You chose " + answer)

pg.alert ("Thanks For Playing.")

webbrowser.open ("https://media.giphy.com/media/GfhdNwgN0Y7N6/giphy.gif")
