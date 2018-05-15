import pyautogui as pg
import webbrowser

gamingvideos = ["https://www.youtube.com/watch?v=-uBcEtBqm9Y","https://www.youtube.com/watch?v=X9Z4BYzbTkE"]
parkourvideos = ["https://www.youtube.com/watch?v=pdAdEl07Xqo","https://www.youtube.com/watch?v=NX7QNWEGcNI"]

answer = pg.prompt(
"""
Which would you rather watch?

a) Gaming Videos
b) Parkour videos

"""
)

if answer == "a": 
    for i in gamingvideos:
        webbrowser.open(i)

elif answer == "b":
    for i in parkourvideos:
        webbrowser.open(i)
