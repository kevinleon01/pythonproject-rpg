#import necessary stuff
import random
import time
from characters import Character, Hero, Villager, Goblin, Zombie, Skeleton
from items import Potion, Poison, Bomb

# initiate characters
goblin  = Goblin( 'The Goblin', 6, 2)
hero = Hero('The Hero', 10, 5, [])
villager = Villager('The Villager', 8, 1, [])
zombie = Zombie('The Zombie', 15, 1)
skeleton = Skeleton('The Skeleton', 6, 3)

#time.sleep(/seconds to wait/)

# initiate items
potion = Potion('potion of health', 9)
poison = Poison('potion of poison', 9)
bomb = Bomb('bomb', 6)

# create supplementary functions
# def use_potion(char):
#         print("You used 'potion'")
#         char.health += potion.health

# def use_poison(char):
#         print("You used poison")
#         if char == 'zombie' or char == 'skeleton':
#             char.health += potion_two.health
#         else:
#             char.health -= potion_two.health  

def use_bomb(char):
    print("You used bomb")
    char.health -= bomb.power


# create print functions
def print_menu():
    print()
    print("What do you want to do?")
    print("1. fight ")
    print("2. do nothing")
    print("3. flee")
    print("4. use item")
    print("> ",)

def print_villager_menu():
    print()
    print("What do you want to do?")
    print("1. fight ")
    print("2. do nothing")
    print("3. leave")
    print("4. use item")
    print("5: ask for item")
    print("> ",)

def print_items(self):
    for items in self.items:
        print("Your items: ")
        print(items)

def print_opener():
    print("""
            ...

You are traveling through the smoky mountains, trying to
reach the village before sundown. 

Suddenly, you cross paths with a goblin who was hiding
among the thicket of trees.
    """)

def print_meeting_villager():
    print("""
You left the previous fight victorious.

            ...

You found your way to the nearest town.
There you meet a (seemingly) kind villager... 
    """)

def print_continuing_on():
    print("""
            ...

You continue on, steadfast, headed for your destination.
    """)

def print_meeting_villager_two():
    print("""
            ...

Out of pure coincidence, you have once again
come across the villager from before.
I suppose they could've gotten ahead of you
while you were tied up with the zombie.

You stop to talk to him before 
continuing forth.
    """)

def print_almost_there():
    print("""
            ...

You see the town lights glowing against the ever-darkening
background. "I'm almost there," you think to
yourself. But before any sense or relief can set in,
You hear the xylophonic rumble of bones...
    """)

def print_made_it():
    print("""
            ...

After what has felt like an eternity since you set off, 
you've finally made it to the safety of the town and
it's lights. You find a quiet room in the local Inn
to rest and recuperate. 

Goodnight.

    """)

# create interaction functions
def goblinfight():
    while goblin.is_alive() and hero.is_alive():
        hero.print_status()
        goblin.print_status()
        print_menu()
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
            if not goblin.is_alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            use = input("Do you want to use an item? (y/n) ").lower()
            if use == 'y':
                if len(hero.items) == 0:
                    print("You do not have any items!")
                    pass
                elif len(hero.items) == 1:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                    elif who_to_use == 2:
                        current_item.use(zombie)
                    else:
                        print("Invalid input %r" % user_input)
        else:
            print("Invalid input %r" % user_input)

        if goblin.is_alive():
            goblin.attack(hero)
            if not hero.is_alive():
                print(f"You were slain by {goblin.name}.")

def zombiefight():
    while zombie.is_alive() and hero.is_alive():
        hero.print_status()
        zombie.print_status()
        print_menu()
        user_input = input()
        if user_input == "1":
            hero.attack(zombie)
            if not zombie.is_alive():
                print("The zombie is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            use = input("Do you want to use an item? (y/n) ").lower()
            if use == 'y':
                if len(hero.items) == 0:
                    print("You do not have any items!")
                    pass
                elif len(hero.items) == 1:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                    elif who_to_use == 2:
                        current_item.use(zombie)
        else:
            print("Invalid input %r" % user_input)

        if zombie.is_alive():
                    zombie.attack(hero)
                    if not hero.is_alive():
                        print(f"You were slain by {zombie.name}.")

def skeletonfight():
    while skeleton.is_alive() and hero.is_alive():
        hero.print_status()
        skeleton.print_status()
        print_menu()
        user_input = input()
        if user_input == "1":
            hero.attack(skeleton)
            if not skeleton.is_alive():
                print("The skeleton is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            use = input("Do you want to use an item? (y/n) ").lower()
            if use == 'y':
                if len(hero.items) == 0:
                    print("You do not have any items!")
                    pass
                elif len(hero.items) == 1:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                        del hero.items[current_item]
                    elif who_to_use == 2:
                        current_item.use(skeleton)
                        del hero.items[current_item]
                    else:
                        print("Invalid input %r" % user_input)
                elif len(hero.items) == 2:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                        del hero.items[current_item]
                    elif who_to_use == 2:
                        current_item.use(skeleton)
                        del hero.items[current_item]
                    else:
                        print("Invalid input %r" % user_input)
        else:
            print("Invalid input %r" % user_input)

        if skeleton.is_alive():
            skeleton.attack(hero)
            if not hero.is_alive():
                print(f"You were slain by {skeleton.name}.")

def villagertalk():
    while villager.is_alive() and hero.is_alive():
        hero.print_status()
        villager.print_status()
        print_villager_menu()
        user_input = input()
        if user_input == "1":
            hero.attack(villager)
            if not villager.is_alive():
                print("The villager is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            use = input("Do you want to use an item? (y/n) ").lower()
            if use == 'y':
                if len(hero.items) == 0:
                    print("You do not have any items!")
                    pass
                elif len(hero.items) == 1:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                    elif who_to_use == 2:
                        current_item.use(villager)
                elif len(hero.items) == 2:
                    print("Which item would you like to use? ")
                    print(hero.items[0])
                    choice = int(input())
                    answer = choice - 1
                    current_item = hero.items[answer]
                    who_to_use = int(input("Who do you want to use the item on? '1' for hero, '2' for enemy"))
                    if who_to_use == 1:
                        current_item.use(hero)
                    elif who_to_use == 2:
                        current_item.use(villager)
        elif user_input == "5":
            item_number = random.randint(1, 4)
            if item_number == 1:
                print("Villager: \"Here you go\"")
                print("""you received as potion of health
                
                \"Goodbye.\"
                """)
                hero.items.append(potion)
                print_items(hero)
                break
            elif item_number == 2:
                print("Villager: \"Here you go\"")
                print("""You received a potion of poison
                
                \"Seeya.\"
                """)
                hero.items.append(poison)
                print_items(hero)
                break
            elif item_number == 3:
                print("Villager: \"Here you go\"")
                print(""""You received a bomb.
                
                \"Later.\"
                """)
                hero.items.append(bomb)
                print_items(hero)
                break
            else:
                print("""Villager: \"Sorry I do not have an item right now...
                
                Goodbye.\"
                """)
                print_items(hero)
                break
        else:
            print("Invalid input %r" % user_input)

# compile story
def main():
    print_opener()
    goblinfight()
    print_meeting_villager()
    villagertalk()
    print_continuing_on()
    zombiefight()
    print_meeting_villager_two()
    villagertalk()
    print_almost_there()
    skeletonfight()
    print_made_it()

# run the game
main()
