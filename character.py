class Character:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.health = 100

    @property
    def in_health(self, increment):
        return self.health + increment

    @property
    def de_health(self, decrement):
        return self.health - decrement

    @property
    def add_inventory(self, item, amount):
        amount += amount
        return self.inventory.append(f"{amount} : {item}")
