# !/usr/bin/env python3
# Monster Name
import time
import os
from sys import platform

stick = None
characterInventory = {}
mName = ""
runOrFight = "a"
answer = "a"

name = input('Before we begin, please enter your name.')


def printDelay(msg, delay):
    print(msg)
    time.sleep(delay)


def addInventory(key, amount):
    global characterInventory
    if key in characterInventory:
        characterInventory[key] = amount
    elif key not in characterInventory:
        characterInventory.update({key: amount})


def playAgain():
    play = input("Do you want to play again?"
                 "Yes(a) or no(b)")
    if play.lower()[:1:] == "a" or play.lower()[:1:] == "y":
        Welcome()
    else:
        printDelay("Okay, bye.", 1)
        return


def Welcome():
    characterInventory.clear()
    print("Welcome to Story Path!")
    time.sleep(1)
    print("In this game, YOU will be the one making the actions, and if YOU die...")
    time.sleep(1)
    print('YOU will be the one taking fault.')
    time.sleep(2)
    print('Are')
    time.sleep(.5)
    print('You')
    time.sleep(.5)
    print('Ready?!?!?!')
    areYouReady = input()
    if areYouReady.lower()[:1:] == "y":
        Start()
    else:
        print("Okay, bye.")
        return


def Start():
    print("Now, let us begin.")
    setting()


# This will be the setting that they are in. If you want to change,
# just rewrite the wording a little bit.
# Should we ask for the name right now, or later?


def setting():
    print('You awake to find yourself stranded in a forest,')
    time.sleep(1)
    print('not knowing where you are, or how you got there.')
    time.sleep(.1)
    print('...')
    time.sleep(1)
    print("You spot a spaceship right next to you.")
    time.sleep(1)
    print("Do you want to investigate the spaceship,"
          "or explore the forest a little bit further?")
    isValidResponse = False
    while not isValidResponse:
        investigateOrExplore = input('investigate or explore?')
        if investigateOrExplore.lower()[:1:] == "i":
            isValidResponse = True
            SpaceshipInvestigation()
        elif investigateOrExplore.lower()[:1:] == "e":
            isValidResponse = True
            mazeForest()
        else:
            print("Invalid try again.")


def mazeForest():
    print("As you walk deeper into the forest, you find yourself getting lost.")
    time.sleep(1)
    print("Soon, you cannot find your way anywhere.")
    time.sleep(1)
    print("You cannot see, and you stumble.")
    time.sleep(1.1)
    printDelay("Your eyesight is hazy,"
               "and your head really hurts.", 1.5)
    print("Do you want to search your pockets (s),"
          "or try to find your way back to the spaceship (f)?")
    isValidResponse = False
    while not isValidResponse:
        SearchOrFind = input()
        if SearchOrFind.lower()[:1:] == "s":
            isValidResponse = True
            SearchPockets()
        if SearchOrFind.lower()[:1:] == "f:":
            isValidResponse = True
            findSpaceship()


def findSpaceship():
    printDelay("When you try to find you way"
               "back to the spaceship, you meet"
               "a dark shape blocking your path.", 3)
    print("Do you want to run away (r),"
          "or try to get around it (g),"
          "or feel amazing and attack it head on (a)?")
    isValidResponse = False
    while not isValidResponse:
        if input().lower()[:1:] == "r":
            isValidResponse = True
            printDelay("After running for some time, you get tired."
                       "Since it is night, and you cannot find your"
                       "way anywhere, you just fall asleep in a "
                       "tree trunk, but you never see the daylight again.", 4.1)
            playAgain()
        if input().lower()[:1:] == "g":
            isValidResponse = True
            printDelay("As you try to sneakily get around it,"
                       "it seems to be working.", 1.25)


def SearchPockets():
    pass


def SpaceshipInvestigation():
    print("When you reach the spaceship, you see a couple of things:")
    time.sleep(1.25)
    print(" 1) A ray gun")
    time.sleep(1)
    print(" 2) A vest, very thick and looking uncomfortable to put on")
    time.sleep(1.5)
    print(" 3) 5 chemical vials")
    time.sleep(1)
    print(" 4) A portable sleeping bag")
    time.sleep(1)
    print(' 5) A bag labeled "food"')
    time.sleep(1)
    print(" 6) a belt labeled 'gravity belt'")
    time.sleep(1)
    print("You see that the cockpit is not that big,"
          "and that even though you have enough supplies,")
    time.sleep(2)
    print("you might find something of use in the cargo space.")
    time.sleep(1.5)
    CargoExplore = input("Do you want to explore(e) or pick up(p)?")
    if CargoExplore.lower()[:1:] == "e":
        meetingMonster()
    elif CargoExplore.lower()[:1:] == "p":
        chooseFromCockpit(None, None, None, None, None, None,)


def meetingMonster():
    print("You hear a noise when you open the cargo crate.")
    monster = input("Do you want to investigate the noise?")
    if monster.lower()[:1:] == "y":
        print("You find a large monster that is snoring."
              "You gently poke it.")
        time.sleep(1.25)
        print("You leave some food in front of it and you sit there and wait.")
        time.sleep(7)
        print("after a while. the monster wakes up, gobbles up the food,"
              "and looks at you.")
        time.sleep(2)
        print("HI. it's great deep voice rumbles around you. (its in caps)")
        time.sleep(1.5)
        print("You believe that he is friendly.")
        time.sleep(1)
        live_with_monster()


def chooseFromCockpit(cannotPick1, cannotPick2, cannotPick3, cannotPick4, cannotPick5, cannotPick6):
    isValidResponse = False
    while not isValidResponse:
        whatPick = input("What do you want to pick up?"
                         "You can only pick up one thing:"
                         "1, 2, 3, 4, 5, or 6?")
        if whatPick == "1":
            if cannotPick1.lower()[:1:] == "r"\
                    or cannotPick2.lower()[:1:] == "r"\
                    or cannotPick3.lower()[:1:] == "r"\
                    or cannotPick4.lower()[:1:] == "r"\
                    or cannotPick5.lower()[:1:] == "r"\
                    or cannotPick6.lower()[:1:] == "r":
                pass
            else:
                isValidResponse = True
                mazeForestSleep()
        elif whatPick == "2":
            isValidResponse = True
            characterInventory.update({"vest": 1})
            mazeForest()
        elif whatPick == "3":
            isValidResponse = True
            printDelay("You burn yourself, and get mutated into a monster.", 1)
            printDelay("The spaceship self-defense system activates and you get shot, and die.", 1.25)
            playAgain()
        elif whatPick == "4":
            characterInventory.update({"port-sleeping bag": 1})
            isValidResponse = True
            mazeForest()  # This we still need to fix.
        elif whatPick == "5":
            characterInventory.update({"food": 5})
            isValidResponse = True
            mazeForest()  # Same here.
        elif whatPick == "6":
            print("You try it on, and nothing happens."
                  "Do you want to pick another item?")
            pickAnotherItem = input()
            if pickAnotherItem.lower()[:1:] == "n":
                isValidResponse = True
                thatIsWhenHeRealized()
            else:
                chooseFromCockpit(None, None, None, None, None, None,)
        else:
            printDelay("Invalid response. Please pick one of the ones above.", 1.25)


def clearScreen():
    if platform == "darwin":
        os.system('clear')
    elif platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def live_with_monster():
    global characterInventory
    global stick
    global runOrFight
    global mName
    print("You decide to befriend him.")
    time.sleep(1)
    print("He befriends you!")
    time.sleep(1)
    mName = input("What do you name him?")
    time.sleep(1)
    print(name + " has befriended " + mName + "!")
    time.sleep(1)
    print("After a while he gives you a stick.")
    time.sleep(1)
    print("You don't know why though...")
    print("The monster points towards Maze Forrest.")
    print("You both walk into the forest.")
    time.sleep(5)
    clearScreen()
    time.sleep(1)
    clearScreen()
    time.sleep(5)
    print("MAZE FOREST")
    printDelay("Here is you inventory.", 1)
    print(characterInventory)
    time.sleep(1)
    printDelay("As you walk through this forest, you realize just how big it is.", 1.5)
    printDelay("You hear sounds that sound like talking.", 1)
    printDelay("You and " + mName + " hide behind a bush.", 1)
    printDelay("You look behind the bush, and see a horde of garblins.", 1.5)
    print("They are half gargoyle, half goblin creatures.")
    time.sleep(1)
    printDelay("And they're usually defending something...", 1.2)
    printDelay("Do you want to fight the garblins, or run away?", 1.2)
    runOrFight = input("run (r) or fight (f)")
    if runOrFight.lower()[:1:] == "r":
        print("You and the monster barely outrun the garblins.")
        tired()
    else:
        print("You and the monster jump out of the bush and succesfully defend against the garblins.")
        print("You walk a bit further in the forrest, and come across a huge temple like structure.")
        time.sleep(5)
        clearScreen()
        print("THE TEMPLE OF THE GARBLINS")
        print("Temple")
        time.sleep(1)
        printDelay("Here is your inventory.", 1)
        printDelay(characterInventory, 4)
        print("As you walk through the temple, you see how old it is.")
        print("You find a first aid kit on the ground with a note on it.")
        print("The note reads,")
        print("To whoever finds this, good luck.")
        print("You pick it up.")
        print("You got a first aid kit.")
        addInventory("FirstAidKit", 1)
        print("As you're walking through the temple, you see a group of garblins that are patrolling the temple.")
        print("Do you want to take a different route or keep goig on the same route?")
        answer = input("take a differnent route(t) or keep going (k)")
        if answer.lower()[:1:] == "t":
            print("")
        else:
            print("")
        # Temporarily ending the function
        return


def tired():
    printDelay("After all of what happened today,"
               "you just want to fall asleep.", 1.75)
    sleep()


def sleep():
    print("You try to sleep.")
    time.sleep(1.5)
    printDelay("You toss and turn, really tired, but since you are so tired,"
               "you cannot sleep.", 1.5)
    printDelay("And you notice a tag that is at the neck of the regoob,"
               "who is really tired.", 1.75)
    tag = input("Do you want to read the tag? yes(y) or no(n)")
    if tag.lower()[:1:] == "y":
        readTag()
    print("You go back to sleep, actually sleeping.")
    # day 2
    time.sleep(5)
    print("The next day...")
    time.sleep(1)
    print("You wake up to find " + mName + " gone!")
    print("You also find yourself chained up!")
    time.sleep(2)
    prison()


def prison():
    print("You're stuck in ropes!")
    print("YOU HAVE BEEN SENTENCED TO BE TIED UP UNTIL YOU READ THE TAG,"
          "FOR IT IS MY DUTY!")
    read = input("Do you want to read the tag?")
    if read.lower()[:1:] == "y":
        readTag()
    else:
        printDelay("The creature that is looking at you now kills itself on the rocks,"
                   "and you, having nothing and no one to untie you,"
                   "fall to the prey of another creature and die.", 4)
        playAgain()


def readTag():
    printDelay("The tag read:", 1)
    print(" This animal is a regoob, and they are very flexible, no skeleton at all!")
    time.sleep(1.5)
    print("But this animal is yours, and if you read this letter, then that means that you")
    time.sleep(1.5)
    print("did the right choice. regoobs are very strict to their instructions,"
          "and this regoob's job was to give you this letter.")
    time.sleep(1.25)
    print("They will tie you up with anything that they have"
          "until their deed is completed with you.")
    time.sleep(2)
    print("What you have to do is find the temples around this world called Yiggurt,"
          "to find the pieces of your past.")
    time.sleep(3)
    journey()


def journey():
    printDelay("THE JOURNEY", 1)
    printDelay("Here is your inventory.", 1)
    printDelay(characterInventory, 1.5)
    printDelay("Now that you now where you are, you set out on the quest.", 3)
    printDelay("You talk to the regoob, and he agrees to help you on the quest.", 0.5)
    printDelay("Now that you realize that this"
               "is your goal,", 1.5)
    printDelay("You set off not knowing where to start.", 1.25)
    printDelay("So you wander about, also wanting to find some food.", 1.5)
    meetingVillage()


def thatIsWhenHeRealized():
    printDelay("as you walk, something tugs a little bit, but not hard."
               " You look down and see a medium sized branch.", 2)
    printDelay("When you lift it from the gravity belt, you almost crumple"
               "from the sudden weight.", 1.5)
    printDelay("When you clip it back onto your gravity belt,"
               "it feels almost weightless.", 2)
    printDelay("This is when you realize you can take more things from the"
               "cockpit this way.", 1.5)
    printDelay("Do you want to take more things from the cockpit? (yes or no)", 1.25)
    isValidResponse = False
    while not isValidResponse:
        if input().lower()[:1:] == "y":
            chooseFromCockpit("gravityBelt", None, None, None, None, None)


def mazeForestSleep():
    printDelay("When you go exploring, you hear your stomach grumble,"
               "thinking that you have to go find food sooner or later.", 2)
    printDelay("But before you go anywhere,"
               "you want to try out the ray gut first.", 1.75)


def meetingVillage():
    global mName
    printDelay("You travel in a direction for 2 days when you stumble a cross a village.", 3)
    printDelay("You notice that" + mName + "is lagging behind, and he looks scared.", 1)
    do = input("Do you ask him why is looks scared?")
    if do.lower()[:1:] == "y":
        printDelay("THE VILLAGE IS A HUNTING VILLAGE,"
                   "AND FINDING US IN THE WILD ARE EXPENSIVE.", 2)
        getShot()
    elif do.lower()[:1:] == "n":
        printDelay("you just walk along, pondering why he is so scared.", 1.5)
        getShot()


def getShot():
    pass


# Is this Welcome() at the end for if the player dies?
# No its to run
Welcome()
