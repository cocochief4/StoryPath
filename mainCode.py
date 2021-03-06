import time
import temple1
import importantStuff
characterInventory = importantStuff.characterInventory
stick = importantStuff.stick
mName = importantStuff.mName
runOrFight = importantStuff.runOrFight

# def add_inventory(key, amount):


def play_again():
    play = input("Do you want to play again?"
                 "Yes(a) or no(b)")
    if play.lower()[:1:] == "a" or play.lower()[:1:] == "y":
        welcome()
    else:
        importantStuff.print_delay("Okay, killing whole program.", 1)
        return


def welcome():
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
    are_you_ready = input()
    if are_you_ready.lower()[:1:] == "y":
        start()
    else:
        print("Okay, bye.")
        return


def start():
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
    is_valid_response = False
    while not is_valid_response:
        investigate_or_explore = input('investigate or explore?')
        if investigate_or_explore.lower()[:1:] == "i":
            is_valid_response = True
            spaceship_investigation()
        elif investigate_or_explore.lower()[:1:] == "e":
            is_valid_response = True
            maze_forest()
        else:
            print("Invalid try again.")


def maze_forest():
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
    play_again()
    time.sleep(1.1)
    importantStuff.print_delay("Your eyesight is hazy, and your head really hurts.", 1.5)
    print("Do you want to search your pockets (s),"
          "or try to find your way back to the spaceship (f)?")
    is_valid_response = False
    while not is_valid_response:
        search_or_find = input()
        if search_or_find.lower()[:1:] == "s":
            is_valid_response = True
            search_pockets()
        if search_or_find.lower()[:1:] == "f:":
            is_valid_response = True
            find_spaceship()


def find_spaceship():
    importantStuff.print_delay("When you try to find you way"
                "back to the spaceship, you meet"
                "a dark shape blocking your path.", 3)
    print("Do you want to run away (r),"
          "or try to get around it (g),"
          "or feel amazing and attack it head on (a)?")
    is_valid_response = False
    while not is_valid_response:
        if input().lower()[:1:] == "r":
            is_valid_response = True
            importantStuff.print_delay("After running for some time, you get tired."
                        "Since it is night, and you cannot find your"
                        "way anywhere, you just fall asleep in a "
                        "tree trunk, but you never see the daylight again.", 4.1)
            play_again()
        if input().lower()[:1:] == "g":
            is_valid_response = True
            importantStuff.print_delay("As you try to sneakily get around it,"
                        "it seems to be working.", 1.25)


def search_pockets():
    pass


def spaceship_investigation():
    importantStuff.clear_screen()
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
    cargo_explore = input("Do you want to explore(e) or pick up(p)?")
    if cargo_explore.lower()[:1:] == "e":
        meeting_monster()
    elif cargo_explore.lower()[:1:] == "p":
        choose_from_cockpit()
        pass
    cargo_explore = input("Do you want to explore(e) or pick up(p)?")
    if cargo_explore.lower()[:1:] == "e":
        meeting_monster()
    elif cargo_explore.lower()[:1:] == "p":
        pass


def choose_from_cockpit():
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
    item_chose = input(importantStuff.print_delay("What do you want from the cockpit?", 1.5))
    if item_chose == 1 or item_chose.lower()[:1:] == "r":
        pass
    elif item_chose == 2 or item_chose.lower()[:1:] == "v":
        pass
    elif item_chose == 3 or item_chose.lower()[:1:] == "c":
        pass
    elif item_chose == 4 or item_chose.lower()[:1:] == "s":
        pass
    elif item_chose == 5 or item_chose.lower()[:1:] == "b":
        pass
    elif item_chose == 6 or item_chose.lower()[:1:] == "g":
        pass


def meeting_monster():
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
        print("HI. It's great deep voice rumbles around you.")
        time.sleep(1.5)
        print("You believe that he is friendly.")
        time.sleep(1)
        temple1.live_with_monster()

# # def choose_from_cockpit(cannot_pick1, cannot_pick2, cannot_pick3, cannot_pick4, cannot_pick5, cannot_pick6):
# #    is_valid_response = False
#     while not is_valid_response:
#         what_pick = input("What do you want to pick up?"
#                           "You can only pick up one thing:"
#                           "1, 2, 3, 4, 5, or 6?")
#         if what_pick == "1":
#             if cannot_pick1.lower()[:1:] == "r"\
#                     or cannot_pick2.lower()[:1:] == "r"\
#                     or cannot_pick3.lower()[:1:] == "r"\
#                     or cannot_pick4.lower()[:1:] == "r"\
#                     or cannot_pick5.lower()[:1:] == "r"\
#                     or cannot_pick6.lower()[:1:] == "r":
#                 pass
#             else:
#                 is_valid_response = True
#                 maze_forest_sleep()
#         elif what_pick == "2":
#             is_valid_response = True
#             characterInventory.update({"vest": 1})
#             maze_forest()
#         elif what_pick == "3":
#             is_valid_response = True
#             print_delay("You burn yourself, and get mutated into a monster.", 1)
#             print_delay("The spaceship self-defense system activates and you get shot, and die.", 1.25)
#             play_again()
#         elif what_pick == "4":
#             characterInventory.update({"port-sleeping bag": 1})
#             is_valid_response = True
#             maze_forest()  # This we still need to fix.
#         elif what_pick == "5":
#             characterInventory.update({"food": 5})
#             is_valid_response = True
#             maze_forest()  # Same here.
#         elif what_pick == "6":
#             print("You try it on, and nothing happens."
#                   "Do you want to pick another item?")
#             pick_another_item = input()
#             if pick_another_item.lower()[:1:] == "n":
#                 is_valid_response = True
#                 that_is_when_he_realized()
#             else:
#                 choose_from_cockpit(None, None, None, None, None, None,)
#         else:
#             print_delay("Invalid response. Please pick one of the ones above.", 1.25)
#
#
# def clear_screen():
#     if platform == "darwin":
#         os.system('clear')
#     elif platform == "linux" or platform == "linux2":
#         # linux
#     elif platform == "win32":
#         os.system('cls')


def sleep():
    print("You try to sleep.")
    time.sleep(1.5)
    importantStuff.print_delay("You toss and turn, really tired, but since you are so wired, you cannot sleep.", 1.5)
    importantStuff.print_delay("And you notice a tag that is at the neck of the regoob, who is really tired.", 1.75)
    importantStuff.print_delay("You toss and turn, really tired, but since you are so tired, you cannot sleep.", 1.5)
    importantStuff.print_delay("And you notice a tag that is at the neck of the regoob, who is really tired.", 1.75)
    tag = input("Do you want to read the tag? yes(y) or no(n)")
    if tag.lower()[:1:] == "y":
        read_tag()
    else:
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
        read_tag()
    else:
        importantStuff.print_delay("The creature that is looking at you now kills itself on the rocks,"
                    " and you, having nothing and no one to untie you, fall to the prey of "
                    "another creature and die.", 4)
        play_again()


def read_tag():
    importantStuff.print_delay("The tag read:", 1)
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
    importantStuff.print_delay("THE JOURNEY", 1)
    importantStuff.print_delay("Here is your inventory.", 1)
    importantStuff.print_delay(characterInventory, 1.5)
    importantStuff.print_delay("Now that you now where you are, you set out on the quest.", 3)
    importantStuff.print_delay("You talk to the regoob, and he agrees to help you on the quest.", 0.5)
    first_town()
    importantStuff.print_delay("Now that you realize that this is your goal,", 1.5)
    importantStuff.print_delay("You set off not knowing where to start.", 1.25)
    importantStuff.print_delay("So you wander about, also wanting to find some food.", 1.5)


def maze_forest_sleep():
    importantStuff.print_delay("When you go exploring, you hear your stomach grumble, "
                "thinking that you have to go find food sooner or later.", 2)
    importantStuff.print_delay("But before you go anywhere, you want to try out the ray gun first.", 1.75)


def first_town():
    importantStuff.print_delay("You travel in a direction for 2 days when you stumble a cross a village.", 3)
    importantStuff.print_delay("You notice that the regoob is lagging behind, and he looks scared.", 1)
    do = input("Do you ask him why is looks scared?")
    if do.lower()[:1:] == "y":
        importantStuff.print_delay("He says that the village is a hunting village, and regoobs are very expensive", 2)
    elif do.lower()[:1:] == "n":
        importantStuff.print_delay("You keep on going thinking that he is just tired.", 1)
        dead_regoob()
    else:
        importantStuff.print_delay("Invalid response: Try Again", 0.5)


def dead_regoob():
    importantStuff.print_delay("You go to the village, and immediately you hear a trap go into action.", 3)
    importantStuff.print_delay("You turn around and see that the regoob has been caught.", 1)
    importantStuff.print_delay("You hide just in time, but you find the regoob being taken away"
                "into the camp. Hear a squelch, and you know it's over.", 4)
    depression()


def depression():
    importantStuff.print_delay("Suffering from depression, you suicide by jumping into a pit of quick sand", 5)


def the_journey():
    play_again()
    importantStuff.print_delay("THE JOURNEY", 1)
    importantStuff.print_delay("Here is your inventory.", 1)
    importantStuff.print_delay(characterInventory, 1.5)
    importantStuff.print_delay("Now that you know what to do, you set out on the quest.", 3)
    importantStuff.print_delay("You talk to the regoob, and he agrees to help you on the quest.", 0.5)
    importantStuff.print_delay("Now that you realize that this is your goal,", 1.5)
    importantStuff.print_delay("You set off not knowing where to start.", 1.25)
    importantStuff.print_delay("So you wander about, also wanting to find some food.", 1.5)
    meeting_village()


def that_is_when_he_realized():
    importantStuff.print_delay("as you walk, something tugs a little bit, but not hard. "
                "You look down and see a medium sized branch.", 2)
    importantStuff.print_delay("When you lift it from the gravity belt, you almost crumple from the sudden weight.", 1.5)
    importantStuff.print_delay("When you clip it back onto your gravity belt, it feels almost weightless.", 2)
    importantStuff.print_delay("This is when you realize you can take more things from the cockpit this way.", 1.5)
    importantStuff.print_delay("Do you want to take more things from the cockpit? (yes or no)", 1.25)
    is_valid_response = False
    while not is_valid_response:
        if input().lower()[:1:] == "y":
            # choose_from_cockpit("gravityBelt", None, None, None, None, None)
            pass

    # while not is_valid_response:
    #     # if input().lower()[:1:] == "y":


# choose_from_cockpit("gravityBelt", None, None, None, None, None)


def meeting_village():
    importantStuff.print_delay("You travel in a direction for 2 days when you stumble a cross a village.", 3)
    importantStuff.print_delay("You notice that" + mName + "is lagging behind, and he looks scared.", 1)
    do = input("Do you ask him why is looks scared?")
    if do.lower()[:1:] == "y":
        importantStuff.print_delay("THE VILLAGE IS A HUNTING VILLAGE, AND FINDING US IN THE WILD WOULD LEAD ME TO DEATH!!.", 2)
        turn_around()
    elif do.lower()[:1:] == "n":
        importantStuff.print_delay("you just walk along, pondering why he is so scared.", 1.5)
        get_shot()


def get_shot():
    print("You ")


def turn_around():
    print("You head back, and you go around the village.")


# Is this Welcome() at the end for if the player dies?
# No its to run
welcome()
