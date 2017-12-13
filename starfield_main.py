# Prerequisites. StarField will not use the OS functionality for harmful purposes, only to clear the console, change colours and change the console title.
import os
import random
import time
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()
os.system('color 0A')
os.system('title Starfield')

# Starting Points, Ammunition, Ship Types, Ship Needs and Crew
rail = 5
guns = 100
crew = 1000
points = 0
shiptypes = ["Galaxy-class cruiser", "Nebula-class long-range traveller", "Nebula-class hauler", "unidentified ship"]

# Functions
def computerload():
    cls()
    loadedPercentage = 0
    while loadedPercentage < 100:
        print("StarField Computer Interface : Loading " + str(loadedPercentage) + "%")
        loadedPercentage = loadedPercentage + 4.353428849 # vary this up
        cls()
    print("StarField Computer Interface : STARTED with 3 errors")
    cls()

def computerload2(sr, lr, rail, guns):
    loadedPercentage = 0
    while loadedPercentage < 100:
        print(compart)
        print("")
        print("Performing short-range scans: " + str(loadedPercentage + 5.8400742) + "%")
        print("Performing long-range scans: " + str(loadedPercentage + 3.1415926) + "%")
        loadedPercentage = loadedPercentage + 3.353428849 # vary this up
        cls()
    print(compart)
    print("")
    if sr == True:
        print("WARNING : Ship detected on short-range scanners.")
        shipdetected = True
    if lr == True:
        print("WARNING : Ship detected on long-range scanners.")
        shipdetected = True
    print("Computer ready.")
    print("-----")
    print("Rail missiles available: " + str(rail))
    print("Gun ammunition: " + str(guns) + "%")

def ShipDetectedFriendlyEnvoy():
    computerload2(True, False, rail, guns)
    storyintercept = """\

    Your short range scanners detect a ship approaching. It's weapons don't seem
    to be armed; however, multiple scans find ample ammunition aboard to destroy
    your ship. What do you do?

    """
    print(storyintercept)
    storyoption = input(friendlyshiphailoptions)
    if storyoption == "1":
        hailship(1, "GobDOBBER")
    if storyoption == "2":
        armweapons(1, False, 0, 0)
    if storyoption == "3":
        armweapons(1, True, 11.4, 1)
    if storyoption == "4":
        selfdestruct()
    print("You did not pick a valid option. Option (1) has been chosen.")
    hailship(1, "GobDOBBER")


def ShipDetectedHostileTorpedo():
    print("TODO") #TODO
    computerload2(True, False, rail, guns)

def chooseEvent(level):
    if level == 1:
        randomevent = random.randrange(2)
        doevent = eventeasy[randomevent]
        doevent()

def hailship(shipfriendlevel, shipname):
    cls()
    print(compart)
    randomship = random.randrange(4)
    shiptype = shiptypes[randomship]
    if shipfriendlevel == 1:
        print("The ship is friendly, and appears to be a " + shiptype + " called " + shipname + ".")
        sacgunammo = random.randrange(51)
        earnsacpoints = random.randrange(150)
        print("The ship needs ammo. Will you sacrifice " + str(sacgunammo) + "% of your gun ammo? You will earn " + str(earnsacpoints) + " points.")
        if yesNoOptions():
            global guns
            guns = guns - sacgunammo
            global points
            points = points + earnsacpoints
            endgame(points)

def yesNoOptions():
    print("1. Yes")
    print("2. No")
    print("3. Let the computer pick.")
    choose = input("Choose an option : ")
    if choose == "1":
        return True
    if choose == "2":
        return False
    if choose == "3":
        randomchoice = random.randrange(2)
        if randomchoice == 0:
            return False
        if randomchoice == 1:
            return True

def armweapons(shipfriendlevel, fire, ammolostgun, ammolostrail):
    #TODO
    print("")

def selfdestruct():
    global crew
    crewdestructed = random.randrange(crew + 1)
    time.sleep(1)
    cls()
    print(selfdestructart)
    print("")
    print("Countdown Started: 20 Minutes to Destruct")
    time.sleep(2)
    print("Crew Warning Issued : Code Black / All Crew To Escape Pods")
    time.sleep(1)
    print("Sector One Confirmed Clear / Escape Pods 23-51 Launched")
    time.sleep(1.5)
    print("Sector Two Confirmed Clear / Escape Pods 76-101 Launched")
    time.sleep(1.5)
    print("Countdown Warning: 1 Minute to Destruct")
    time.sleep(1.5)
    print("Countdown Warning: 30 Seconds to Destruct")
    time.sleep(2)
    print("Destruct in 3 Seconds")
    time.sleep(1)
    print("Destruct in 2 Seconds")
    time.sleep(1)
    print("Destruct in 1 Second")
    time.sleep(1)
    print("Destruct Initiat-")
    time.sleep(1)
    endgamepoints = points - crewdestructed
    crew = crew - crewdestructed
    endgame(endgamepoints)

def endgame(pts):
    cls()
    print(endgameart)
    print("The game ended. You ended the game with " + str(pts) + " points and had " + str(crew) + " crew.")
    input("Press ENTER to exit.")
    exit()

def optionsmenu():
    print(mainart)
    print("This options menu is underway.")

def eventmenu():
    cls()
    print("This is a developer menu to pick an event. If you are not a dev, restart the game. You can pick from:")
    print("Easy events: " + str(eventeasy))
    print("Hard events: " + str(eventhard))
    print("Extreme events: " + str(eventextreme))
    print("Must-die events: " + str(eventmustdie))
    print("Self-destruct: selfdestruct")
    eventinput = input()
    if eventinput == "ShipDetectedFriendlyEnvoy":
        ShipDetectedFriendlyEnvoy()
    if eventinput == "friendenv":
        ShipDetectedFriendlyEnvoy()
    elif eventinput == "ShipDetectedHostileTorpedo":
        ShipDetectedHostileTorpedo()
    elif eventinput == "endgame":
        endgame("[DEVELOPER CALLED ENDGAME]")


# Event Lists
eventeasy = [ShipDetectedFriendlyEnvoy, ShipDetectedHostileTorpedo]
eventhard = []
eventextreme = []
eventmustdie = []

# Art.
mainart = """\
+----------------------------------------------------------------------+
|                              StarField                               |
|                           Version 1.0 Beta                           |
|                           CHOOSE AN OPTION                           |
|                       Made by @jacksonsevendelta                     |
+----------------------------------------------------------------------+
"""

startart = """\
+----------------------------------------------------------------------+
|                              StarField                               |
|                           Version 1.0 Beta                           |
|                         PRESS ENTER TO START                         |
|                       Made by @jacksonsevendelta                     |
+----------------------------------------------------------------------+
"""

endgameart = """\
+----------------------------------------------------------------------+
|                              StarField                               |
|                           Version 1.0 Beta                           |
|                             End Of Game                              |
|                       Made by @jacksonsevendelta                     |
+----------------------------------------------------------------------+

"""

compart = """\
+----------------------------------------------------------------------+
|                      StarField Computer Interface                    |
|                     Build 90973a, Starship Edition                   |
|                           CHOOSE AN OPTION                           |
+----------------------------------------------------------------------+
"""

selfdestructart = """\
+----------------------------------------------------------------------+
|                      StarField Computer Interface                    |
|                     Build 90973a, Starship Edition                   |
|                    SELF DESTRUCT SEQUENCE INITIATED                  |
+----------------------------------------------------------------------+
"""

friendlyshiphailoptions = """\
1. Hail the ship. You may be able to work out a trade
2. Arm weapons, but don't fire.
3. Arm weapons, and fire. You will lose 11.4% of your gun ammunition and 1 rail
missile
4. Self-destruct your ship. You will gain 1000 points but lose a random number
for the crew that don't make it to escape pods.

Choose an option:
"""

# Game
print(startart)
print()
print('You are the captain of a ship travelling through space. You have 1000 crew members, and it is your duty to')
print('keep them alive. Other ships may approach you, and the may signify danger or opportunity (more points')
print('or resources). Every crew member lost at the end of the game loses you a point, so be careful!')
print()
options = input('Press ENTER to start a new game, or type "other" then ENTER to access an options menu: ')
if options == "other":
    optionsmenu()
elif options == "f":
    eventmenu()
elif options == "exit":
    exit()

computerload()
chooseEvent(1)
