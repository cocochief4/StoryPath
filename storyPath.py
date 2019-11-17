import time


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
# def liveWithMonster():


def playerName():
    name = input('Before we begin, please enter your name.')
    print("Now, let us begin.")
    setting()


def playAgain():
    print("Do you want to play again?")
    play = input("yes or no?")
    while play == 'yes':
        Welcome()


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
    print("And you die. The End.")
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
    CargoExplore = input("Do you want to (explore) or (pick up) and go deeper in the forest?")
    CargoExplore =  input("Do you want to (explore) or (pick up)?")
    CargoExplore = input("Do you want to (explore) or (pick up)?")
    if CargoExplore == "explore":
        meetingMonster()
    elif CargoExplore == "pick up" or CargoExplore == "Pick Up":
        MazeForest()


def Welcome():
    print("Welcome to Story Path!")
    time.sleep(1)
    print("In this game, YOU will be the one making the actions, and if YOU die...")
    time.sleep(1)
    print('YOU will be the one taking fault.')
    time.sleep(2)
    print('Are')
    time.sleep(.25)
    print('You')
    time.sleep(.25)
    print('Ready?!?!?!')
    areYouReady = input()
    if areYouReady == "yes":
        playerName()


Welcome()

=======
#!/usr/bin/env python3
#!/usr/bin/env python3
import time

# Monster Name
mName = ""

name = input('Before we begin, please enter your name.')


import time


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
# def liveWithMonster():



def playerName():
    name = input('Before we begin, please enter your name.')
    print("Now, let us begin.")
    setting()


def playAgain():
    print("Do you want to play again?")
    play = input("yes or no?")
    while play == 'yes':
        Welcome()


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
    print("And you die. The End.")
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
    CargoExplore =  input("Do you want to (explore) or (pick up)?")
    CargoExplore = input("Do you want to (explore) or (pick up)?")
    if CargoExplore == "explore":
        meetingMonster()
    elif CargoExplore.lower()[:1:] == "p":
        whatPick = input("What do you want to pick up? You can only pick up one thing: 1, 2, 3, 4, 5, or 6?")
        if whatPick == "1":
            MazeForest()
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


def Welcome():
    print("Welcome to Story Path!")
    time.sleep(1)
    print("In this game, YOU will be the one making the actions, and if YOU die...")
    time.sleep(1)
    print('YOU will be the one taking fault.')
    time.sleep(2)
    print('Are')
    time.sleep(.25)
    print('You')
    time.sleep(.25)
    print('Ready?!?!?!')
    areYouReady = input()
    if areYouReady == "yes":
        playerName()


Welcome()
