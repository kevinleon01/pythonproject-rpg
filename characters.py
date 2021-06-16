class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def is_alive(self):
        return self.health > 0

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power")

    def attack(self, other_char):
        other_char.health -= self.power
        print(f"{self.name} did {self.power} damage to the enemy.")

class Undead(Character):
    undead = True

#set up charcater subclasses
class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Hero(Character):
    def __init__(self, name, health, power, items):
        self.name = name
        self.health = health
        self.power = power
        self.items = items
        items = []

class Zombie(Undead):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Villager(Character):
    def __init__(self, name, health, power, items):
        self.name = name
        self.health = health
        self.power = power
        self.items = items
        items = []

class Skeleton(Undead):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power