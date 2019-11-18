

# !/usr/bin/env python3
import time

# Monster Name
mName = ""

name = input('Before we begin, please enter your name.')


def printDelay(msg, delay):
    print(msg)
    time.sleep(delay)


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
        liveWithMonster()


def playerName():
    print("Now, let us begin.")
    setting()


def liveWithMonster():
    global mName
    print("You decide to befriend him.")
    time.sleep(1)
    print("He befriends you!")
    time.sleep(1)
    mName = input("What do you name him?")
    time.sleep(1)
    print(name + " has befriended " + mName + "!")
    sleep()
    return mName


def playAgain():
    print("Do you want to play again?")
    play = input("yes(a) or no(b)?")
    while play.lower()[:1:] == "a" or play.lower()[:1:] == "y":
        Welcome()


def sleep():
    print("When you sleep next to it, you notice that it has a tag on it.")
    time.sleep(1.5)
    tag = input("Do you want to read the tag? yes(a) or no(b)")
    while tag == "yes":
        readTag()
    print("You go back to sleep")
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


def readTag():
    print("The tag read:")
    print(" This animal is a regoob, and they are very flexible, no skeleton at all!")
    time.sleep(1.5)
    print("But this animal is yours, and if you read this letter, then that means that you")
    time.sleep(1.5)
    print("did the right choice. regoobs are very strict to their instructions.")
    time.sleep(1.25)
    print("They will tie you up with anything that they have"
          "until their deed is completed with you.")
    time.sleep(2)
    print("What you have to do is find the temples around this world called Yiggurt,"
          "to find the pieces of your past.")


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
    investigateOrExplore = input('investigate or explore?')
    if investigateOrExplore.lower()[:1:] == "i":
        SpaceshipInvestigation()
    elif investigateOrExplore.lower()[:1:] == "e":
        MazeForest()
    else:
        print("Invalid try again.")


def MazeForest():
    print("As you walk deeper into the forest, you find yourself getting lost.")
    time.sleep(1)
    print("Soon, you cannot find your way anywhere.")
    time.sleep(1)
    print("You cannot see, and you stumble.")
    time.sleep(1)
    print("You crash into a tree, and receive a bad concussion.")
    time.sleep(1)
    print("Your brain bleeding internally,")
    time.sleep(.5)
    print("you die. The End.")
    playAgain()


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
        whatPick = input("What do you want to pick up? You can only pick up one thing: 1, 2, 3, 4, 5, or 6?")
        if whatPick == "1":
            MazeForestSleep()
        elif whatPick == "2":
            MazeForest()
        elif whatPick == "3":
            printDelay("You burn yourself, and get mutated into a monster.", 1)
            printDelay("The spaceship self-defense system activates and you get shot, and die.", 1.25)
            playAgain()
        elif whatPick == "4":
            MazeForest()
        elif whatPick == "5":
            MazeForest()
        elif whatPick == "6":
            print("You try it on, and you float!")
            MazeForest()


def MazeForestSleep():
    print("When you go exploring, you hear your stomach grumble,"
          "thinking that you have to go find food sooner or later.")
    print("But before you go anywhere,"
          "you want to try out the ray gut first.")
    print("Remembering ")


def Welcome():
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
    while areYouReady.lower()[:1:] == "y":
        playerName()


Welcome()