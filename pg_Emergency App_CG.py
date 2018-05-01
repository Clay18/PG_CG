import pyautogui as pg
import time
import webbrowser



#Questions goes here
answer = pg.prompt(
"""
What is your adress?

"""
    )
pg.alert ("You chose " + answer)

#Answers go here


#Questions goes here
answer = pg.prompt(
"""
What Happend?

a) Fire

b) Burgler

c) Health


"""
    )
pg.alert ("You chose " + answer)

#Answers go here

if answer == "a":
    pg.alert ("""If you hear a smoke alarm or discover a fire
try not to panic
tell everyone in the house
using your pre-planned escape route, get everyone out of the building as quickly as possible
smoke rises so stay low or crawl on the floor in the cleaner air where it's easier to breathe
don't stop to collect any valuables or possessions
don't stop to look for pets
if possible, close the door to the room where the fire is located and close all doors behind you as you leave (to delay the spread of fire and smoke)
before opening a closed door, touch it with the back of your hand; don't open it if feels warm - the fire will be on the other side
Don't go back into the building
find somewhere safe near the building and wait for the fire service to arrive
if someone is still inside the building, tell the fire service and give details
don't go back into the building; you'll prevent the fire service from doing what they need to do and put your own life at risk too""")

elif answer == "b":
    pg.alert ("""Make a plan – now.  There is no single best strategy.  Some people can climb out a window and run for help…others live or sleep on upper floors and are unable to flee for physical reasons.  If you can safely escape and get help – do it. Be very quiet and listen.  How many intruders are there?  Are they ransacking the house?  Are they making their way toward you?

Don’t argue with your spouse about what to do.  This alerts the intruder to where you are.

Don’t leave your bedroom with a bat or a flashlight.  A surprised intruder is likely to react violently.  You have better options available to you than attempting to confront the intruder.  If you have family to protect you cannot protect them if the intruder gets past you.

Get to a safe place.  A safe room is one of the best options.  Unlike what you have seen in the movies, it doesn’t have to be large and filled with gadgets.  An interior closet with a sturdy door that opens out is just fine.  Put a deadbolt lock on the inside of the door and, most important, recharge your cell phone in there every night.  Then, if you do hear someone in your home, you can go in the closet, lock it and call the police.  Even if the intruder takes a phone off the hook to prevent you from calling for help, you will be able to call the police.  You should be safe until the police arrive.

If you don’t have a safe room, gather your family in a room, lock the door and barricade it with furniture and other heavy objects.  Choose the most secure room with the best door and lock, stay there.

Make sure you have a charged cell phone.  Program your automatic-dial phones to call 911.  It’s difficult to push even three buttons when you’re panicked and your hands are shaking.  Tell the police dispatcher your address and situation in a few sentences.  Be specific.

Example: “Someone has just broken into my house.  It sounds like one person.  I don’t know if he has a weapon.  He’s downstairs in the living room.  I’m upstairs in the master bedroom with my wife.”

Leave the phone line open so the dispatcher can listen to what is happening.

If the intruder reaches the room and turns the doorknob, be prepared to act.  Do not call out, “I’ve called the police.”  By doing so, you will give away your location.  Your bedroom door should have a lock.

Encountering The Intruder

Remain calm and cooperative if the intruder confronts you.  How you behave in the first 30 seconds can set the tone for all that follows.  When violence does occur, it almost always does within these first few moments.

Speak in as normal a voice as you can.  Make no sudden moves.  Tell him that you will cooperate.  Hold your hands up to shoulder level.  It appears compliant, yet it affords you the ability to have your hands ready for defense.

Avoid direct eye contact.  The intruder may interpret this as aggressive behavior and worry that you’ll be able to identify him later.

The outcome of a break-in depends on the intruders.  Most burglars will flee unless they are surprised or confronted.

Home invasion robberies – a small but growing trend – can last for hours and are always violent.  They are carried out by thugs who try to intimidate home owners into divulging dafe combinations and bank ATM personal identification numbers, and handling over credit cards that can’t be reported stolen while the owners are being held hostage.

Create a distress code with your burglar-alarm company.  If you are being held and your alarm has been triggered, you can signal trouble when its representative calls to authenticate the alarm.  Your signal might be, “No, I can’t meet you tomorrow.”  Or just don’t pick up the call, so the company will send the police.

The Weapons Options

It’s your right and personal choice to own a firearm.  People generally aren’t willing to shoot when they need to.  You must be trained properly mentally as well as physically.  Guns are fired in less than 2% of home-intruder situations but a criminal seeing the weapon and fleeing are in dramatically higher percentages.  Also, you need to keep the gun loaded and nearby for it to be effective.  With children living in or visiting your home you need to have an adequate safe to allow you access and still keep the weapon from children.

If you have pepper spray (oleoresin capsicum, or OC), only use it if you need help to escape.  Facial contact and inhalation of the spray will induce up to 45 minutes of coughing, choking, nausea and temporary blindness.  Even residual fumes can make your hiding place unbearable and can be hazardous to people with respiratory and heart conditions.

Your local police department can tell you if you legally can buy pepper spray in your state and where to learn how to use it.  As with any weapon you must have a plan and be prepared to use it.

If You Fight

Never take aggressive action unless you believe that you are in a life-threatening situation.  Escape almost always is the better option.

If you decide to fight back, look for an opportunity when the intruder lets down his guard.  Use a hard object to strike his eyes or throat as fast and hard as you can.  Don’t worry about inflicting injury.  Run as soon as he’s stunned, and yell to get someone’s attention.  The intruder would rather escape than become the center of attention.

Preventing Trouble

Many break-ins can be avoided.  Prevention begins with strong doors.  Most burglaries and break-ins occur through the front door (34%) or the back door (22%).

Install steel-covered solid wood doors that are at least 1.75 inches thick.  Make sure the doorjamb is steel as well.  Any glass panels in or near your doors should be made of unbreakable glass.""")

#Questions goes here
elif answer == "c":
    pg.alert ("""Is it heartburn, or a heart attack?

The most common sign of a heart attack – for both men and women – is chest pain. But knowing whether the pain is a true warning sign of heart attack or a bout of indigestion may not always be obvious.

If your pain is similar to heartburn, but it seems worse or different than what you normally experience, you should get emergency help. This is especially important if you're experiencing other symptoms such as shortness of breath, sweating, dizziness, nausea or pain that moves into your shoulder and arm.

It’s best to pay attention when something does not feel right. It’s better to visit an ER and find out it’s simply heartburn than to ignore the symptoms and find out too late that it’s serious.

Heart attacks in women

Every 42 seconds, someone in the United States suffers a heart attack. Women account for nearly half of all heart attack deaths. Over a life time, heart disease kills five times as many women as breast cancer.

While heart disease is the leading cause of death for both men and women in the United States, there are some key differences between genders. Women tend to experience heart attacks about 10 years later in life than men. Also, women are twice as likely as men to die within the first few weeks after suffering a heart attack.

However, there are many things you can do to help lower your risk of having a heart attack, including being physically active, maintaining a healthy weight, following a healthy diet and knowing your risks.""")

pg.alert ("We are coming as fast as we can.")

webbrowser.open ()

# Source https://www.suffolk.gov.uk/suffolk-fire-and-rescue-service/fire-safety-in-the-home/in-the-event-of-fire-in-your-house/
# Source http://www.citizendefensetraining.com/safe_at_home.htm
# Source https://www.bayeraspirin.com/surviving-a-heart-attack/warning-signs-symptoms/heart-attack-symptoms/?gclid=EAIaIQobChMIwvLm1ODk2gIV1FqGCh2uPwojEAAYASAAEgLfWfD_BwE&gclsrc=aw.ds&dclid=CJbqgNjg5NoCFRaZyAodpCoD5Q
