#!/usr/bin/env python3

import time
name = input('Before we begin, please enter your name.')


def meetingMonster():
    print("You hear a noise when you open the cargo crate.")
    monster = input("Do you want to investigate the noise?")
    if monster == "yes" or monster == "Yes":
        print("You find a large monster that is snoring. \n You gently poke it.")
        print("ou leave some food in front of it and you sit there and wait.")
        print("after a while. the monster wakes up, gobbles up the food, and looks at you.")
        print("He says hi.")
        print("You believe that he is friendly")
        liveWithMonster()


def playerName():
    print("Now, let us begin.")
    setting()


def liveWithMonster():
    print("You decide to befriend him.")
    print("He befriends you")
    mName = input("What do you name him?")
    print(name + " has befriended " + mName + "!")
    sleep()


def playAgain():
    print("Do you want to play again?")
    play = input("yes or no?")
    while play == 'yes':
        Welcome()


def sleep():
    print("When you sleep next to it, you notice that it has a tag on it.")
    tag = input("Do you want to read the tag?")
    if tag == "Yes" or tag == "yes":
        readTag()
    elif tag == "No" or tag == "no":
        print("You go back to sleep")


def readTag():
    print("The tag read:")
    print(" This animal is a regoob, and they are very flexible, no skeleton at all!")
    print("But this animal is yours, and if you read this letter, then that means that you")
    print("did the right choice. regoobs are very strict to their instructions.")
    print("They will tie you up with anything that they have until their deed is completed with you.")
    print("What you have to do is find the temples around this world called Yiggurt, and to find the pieces of your "
          "past.")

        
# This will be the setting that they are in. If you want to change, just rewrite the wording a little bit.
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
    print('Do you want to investigate the spaceship, or explore the forest a little bit further?')
    investigateOrExplore = input('investigate, or explore?')
    if investigateOrExplore == "investigate":
        SpaceshipInvestigation()
    elif investigateOrExplore == "explore":
        MazeForest()


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
    print(" 1) A ray gun")
    print(" 2) A vest, very thick and looking uncomfortable to put on")
    print(" 3) 5 chemical vials")
    print(" 4) A portable sleeping bag")
    print(' 5) A bag labeled"food"')
    print(" 6) a belt labeled 'gravity belt'")
    print("You see that the cockpit is not that big, and that even though you have enough supplies,")
    print("you might find something of use in the cargo space.")
    CargoExplore = input("Do you want to (explore) or (pick up)?")
    if CargoExplore == "explore":
        meetingMonster()
    elif CargoExplore == "pick up":
        MazeForest()


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
    if areYouReady == "yes":
        playerName()


Welcome()
