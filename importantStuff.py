import time
import os
import character
from sys import platform
stick = None
characterInventory = []
mName = ""
runOrFight = "a"
answer = "a"
name = input('Before we begin, please enter your name.')
player = character.Character(name, characterInventory)


def print_delay(msg, delay):
    print(msg)
    time.sleep(delay)


def clear_screen():
    if platform == "darwin":
        os.system('clear')
    elif platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def add_inventory(key, amount):
    if key in characterInventory:
        characterInventory[key] = amount
    else:
        characterInventory.update({key: amount})



