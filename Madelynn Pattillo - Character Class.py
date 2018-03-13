import random


class Characters(object):
    def __init__(self, name, description, abilities, dialogue):
        self.name = name
        self.description = description
        self.health = 100
        self.abilities = abilities
        self.dialogue = dialogue

    def talk(self):
        print("Hello, my name is %s" % self.name)
        print(self.dialogue)

    def view(self):
        print(self.description)

    def attack(self):
        offence = random.randint(1, 10)
        while self.health > 0:
            if offence >= 5:
                print("%s uses %s against their opponent and hits them." % (self.name, self.abilities))
            else:
                print("%s nearly misses their opponent." % self.name)

    def take_damage(self):
        defense = random.randint(1, 10)
        while self.health > 0:
            if defense <= 5:
                self.health = self.health - 5
                print("%s is hit. They now have %d percent of their health." % (self.name, self.health))
            else:
                print("%s dodges the hit. They have %d percent of their health." % (self.name, self.health))
        if self.health == 0:
            print("%s is dead." % self.name)
