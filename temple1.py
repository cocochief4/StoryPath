import time
import random
import storyPath


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
    print(storyPath.name + " has befriended " + mName + "!")
    time.sleep(1)
    print("After a while he gives you a stick.")
    time.sleep(1)
    print("You don't know why though...")
    print("The monster points towards Maze Forrest.")
    print("You both walk into the forest.")
    time.sleep(5)
    storyPath.clear_screen()
    time.sleep(1)
    storyPath.clear_screen()
    time.sleep(5)
    print("MAZE FOREST")
    storyPath.print_delay("Here is you inventory.", 1)
    print(characterInventory)
    time.sleep(1)
    storyPath.print_delay("As you walk through this forest, you realize just how big it is.", 1.5)
    storyPath.print_delay("You hear sounds that sound like talking.", 1)
    storyPath.print_delay("You " + mName + "hide behind a bush.", 1)
    storyPath.print_delay("You look behind the bush, and see a horde of garblins.", 1.5)
    storyPath.print_delay("As you walk through this forest, you realize just how big it is.", 1.5)
    storyPath.print_delay("You hear sounds that sound like talking.", 1)
    storyPath.print_delay("You and " + mName + " hide behind a bush.", 1)
    storyPath.print_delay("You look behind the bush, and see a horde of garblins.", 1.5)
    print("They are half gargoyle, half goblin creatures.")
    time.sleep(1)
    storyPath.print_delay("And they're usually defending something...", 1.2)
    storyPath.print_delay("Do you want to fight the garblins, or run away?", 1.2)
    runOrFight = input("run (r) or fight (f)")
    if runOrFight.lower()[:1:] == "r":
        print("You and the monster barely outrun the garblins.")
        storyPath.tired()
    else:
        print("You and the monster jump out of the bush and succesfully defend against the garblins.")
        print("You walk a bit further in the forrest, and come across a huge temple like structure.")
        time.sleep(5)
        storyPath.clear_screen()
        print("THE TEMPLE OF THE GARBLINS")
        print("Temple")
        time.sleep(1)
        storyPath.print_delay("Here is your inventory.", 1)
        storyPath.print_delay(characterInventory, 4)
        print("As you walk through the temple, you see how old it is.")
        print("You find a first aid kit on the ground with a note on it.")
        print("The note reads,")
        print("To whoever finds this, good luck.")
        print("You pick it up.")
        print("You got a first aid kit.")
        storyPath.add_inventory("FirstAidKit", 1)
        print("As you're walking through the temple, you see a group of garblins that are patrolling the temple.")
        print("Do you want to take a different route or keep goig on the same route?")
        differentRoute = input("take a different route(t) or keep going (k)")
        if differentRoute.lower()[:1:] == "t":
            storyPath.print_delay("", 0)
        else:
            print("you keep hearing the sounds of garblins.")
        # Temporarily ending the function
        return
live_with_monster()