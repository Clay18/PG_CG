import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")

speak.Speak ("What's your favorite NFL team?")

answer = pg.prompt ("Enter your favorite NFL team.")

if answer == "Steelers":
    speak.Speak ("Your obviouslly a human.")

elif answer == "Ravens":
    speak.Speak ("Your not relevent to this universe.")

elif answer == "Patriots":
    speak.Speak ("Band Wagon")

elif answer == "Giants":
    speak.Speak ("Feels Bad")


speak.Speak ("What video do you want to watch?")

video = pg.prompt ("Enter the video below.")

speak.Speak ("OK, let's go find some " + video + " on Youtube.")

wb.open ("https://www.youtube.com/results?search_query=" + video)



