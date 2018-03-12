import random


class Characters(object):
    def __init__(self, name, description, abilities, dialogue):
        self.name = name
        self.description = description
        self.health = 100
        self.abilities = abilities
        self.dialogue = dialogue

    def talk(self):
        print(self.dialogue)

    def attack(self):
        offence = random.randint(1, 10)
        while self.health > 0:
            if offence >= 5:
                print("%s charges toward their opponent and hits them." % self.name)
            else:
                print("%s nearly misses their opponent." % self.name)

    def take_damage(self):
        defense = random.randint(1, 10)
        while self.health > 0:
            if defense >= 5:
                self.health = self.health - 5
                print("%s was hit. They now have %d percent of their health." % (self.name, self.health))
            else:
                print("%s dodged the hit. They have %d percent of their health." % (self.name, self.health))
        if self.health == 0:
            print("%s is dead." % self.name)
