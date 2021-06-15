class Items:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def use(self, other_char):
        other_char.health += self.health
        other_char.power += self.power

class Potion(Items):
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Bomb(Items):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
