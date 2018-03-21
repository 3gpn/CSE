import random


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def view(self):
        print(self.description)

    def hold(self):
        print("You put %s in your inventory." % self.name)


class Diary(Item):
    def __init__(self, description, pages):
        super(Diary, self).__init__("The Diary of Tom M. Riddle", description)
        self.pages = pages
        self.health = 100

    def read(self):
        print("You open the Diary. It says,")
        print(self.pages)

    def talk(self):
        print("You write in the diary")

    def take_damage(self):
        if self.health > 0:
            print("You destroyed the %s" % self.name)


class Cup(Item):
    def __init__(self, description):
        super(Cup, self).__init__("The Cup of Helga Hufflepuff", description)
        self.health = 50

    def take_damage(self):
        if self.health > 0:
            print("You destroyed the %s" % self.name)


class Book(Item):
    def __init__(self, name, description, pages):
        super(Book, self).__init__(name, description)
        self.pages = pages

    def read(self):
        print("You open up %s. It says," % self.name)
        print(self.pages)


class Key(Item):
    def __init__(self, name, description):
        super(Key, self).__init__(name, description)

    def use(self):
        print("You place the %s into the key hole of the door and turn it." % self.name)
        print("The door unlocks.")


class Snitch(Item):
    def __init__(self, description):
        super(Snitch, self).__init__("The Golden Snitch", description)
        self.speed = 100

    def fly(self):
        print("The %s's wings shoot out from it sides and it flutters around your head "
              "at %d mph." % (self.name, self.speed))

    def catch(self):
        print("You jump up and catch %s with great speed, similar to that of a seeker." % self.name)


class Port_Key(Item):
    def __init__(self, name, description):
        super(Port_Key, self).__init__(name, description)

    def teleport(self):
        print("You touch %s and it takes you to another room." % self.name)


class Weapon(Item):
    def __init__(self, name, description, durance, damage):
        super(Weapon, self).__init__(name, description)
        self.durance = durance
        self.damage = damage

    def attack(self):
        offense = random.randint(1, 10)
        if offense >= 5:
            print("You directly hit your opponent with %s" % self.name)
        else:
            print("You missed and angered your opponent.")

    def take_damage(self):
        defense = random.randint(1, 10)
        hit = self.durance - self.damage
        if defense >= 5:
            print("%s is not affected by your opponent's hit. It's durance is %d" % (self.name, self.durance))
        else:
            print("%s took damage from that last hit. Its durance is now %d" % (self.name, hit))

    def health(self):
        if self.durance > 0:
            print("%s is in good condition." % self.name)
        else:
            print("%s was destroyed in the battle. You can no longer use it." % self.name)


class Wand(Weapon):
    def __init__(self, description):
        super(Wand, self).__init__("Wand", description, 100, 5)
        self.spell = ['asendio', 'expelliramus', 'avada kedavra', 'sectum sempra']

    def attack(self):
        offense = random.randint(1, 10)
        distance = random.randint(1, 100)
        spell = input("Pick a spell: %s" % self.spell)
        if offense >= 5 and distance <= 40:
            print("Your wand flickers as it sends %s towards your opponent and hits them." % spell)
        elif offense >= 5 and distance > 40:
            print("Your opponent is too far away. You missed.")
        else:
            print("You missed and angered your opponent.")


class Close(Weapon):
    def __init__(self, name, description, durance, damage):
        super(Close, self).__init__(name, description, durance, damage)

    def attack(self):
        offense = random.randint(1, 10)
        distance = random.randint(1, 20)
        if offense >= 5 and distance <= 10:
            print("You charge at your opponent and hit them with your %s" % self.name)
        elif offense >= 5 and distance > 10:
            print("Your opponent is too far away. Move toward them with caution.")
        else:
            print("Your opponent dodged your attack.")


class Sword(Close):
    def __init__(self, description):
        super(Sword, self).__init__("The Sword of Godric Gryffindor", description, '200', '20')

    def attack(self):
        offense = random.randint(1, 10)
        distance = random.randint(1, 20)
        if offense >= 5 and distance <= 10:
            print("You charge at your opponent and slice them with the blade of %s" % self.name)
        elif distance > 10:
            print("Your opponent is too far away. Move toward them with caution.")
        elif offense == 10 and distance <= 10:
            print("You stab your opponent directly in the center of the chest. They are dead.")
        else:
            print("Your opponent dodged your attack.")


class Club(Close):
    def __init__(self, description, durance, damage):
        super(Club, self).__init__("The Troll's Club", description, durance, damage)


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)

    def eat(self):
        print("You take %s out of your bag and eat it." % self.name)


class Gillyweed(Consumable):
    def __init__(self, description):
        super(Gillyweed, self).__init__("Gillyweed Plant", description)
        self.time = 60

    def eat(self):
        print("You pull the %s out of your bag and place it in your mouth. It will last for 1 hour." % self.name)

    def swim(self):
        print("You get in the water and gills sprout out of your cheeks because of the %s. You have an hour before you "
              "run out of air." % self.name)


class Fried_Chicken(Consumable):
    def __init__(self, description):
        super(Fried_Chicken, self).__init__("Ron's Fried Chicken", description)
        self.health = 25

    def eat(self):
        print("You naw on %s until there is no meat left on the bone. Your health is now replenished." % self.name)


class Potion(Consumable):
    def __init__(self, name, description):
        super(Potion, self).__init__(name, description)


class Tear(Potion):
    def __init__(self, description):
        super(Tear, self).__init__("Phoenix Tear", description)
        self.health = 75

    def pour(self):
        print("You pour the %s on your wounds. You gain 75 health points." % self.name)


class Healing_Potion(Potion):
    def __init__(self, description):
        super(Healing_Potion, self).__init__("Healing Potion", description)
        self.health = 50

    def drink(self):
        print("You pour the %s into your mouth. You gain 50 health points." % self.name)


class Lucky_Potion(Potion):
    def __init__(self, description):
        super(Lucky_Potion, self).__init__("Felix Felices", description)
        self.time = 144
