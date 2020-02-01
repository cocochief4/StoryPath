stick = None
characterInventory = {}
mName = ""
runOrFight = "a"
answer = "a"


def print_delay(msg, delay):
    print(msg)
    time.sleep(delay)


def tired():
    print_delay("After all of what happened today, you just want to fall asleep.", 1.75)
    sleep()


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
    elif key not in characterInventory:
        characterInventory.update({key: amount})


name = input('Before we begin, please enter your name.')
