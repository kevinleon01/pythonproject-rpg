class Items:
    def use(self, other_char):
        other_char.health += self.health
        other_char.power += self.power

class Potion(Items):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def use(self, other):
        if hasattr(other,"undead"):
            other.health -= self.health
            print(f"{other.name} health descreased to {other.health}")
        else:
            other.health += self.health
            print(f"{other.name} health increased to {other.health}")

class Poison(Items):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def use(self, other):
        if hasattr(other,"undead"):
            other.health += self.health
            print(f"{other.name} health increased to {other.health}")
        else:
            other.health -= self.health
            print(f"{other.name} health decreased to {other.health}")

class Bomb(Items):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.health = 0 
    
    def use(self, other):
        other.health -= self.power
        print(f"{other.name} health decreased to {other.health}")



    #def __str__(self):
    # return f'''
    # ====== Pet: {self.name} ======
    # ====== Happiness: {self.happiness} ======
    # ====== Hunger: {self.fullness} ======
    # '''
