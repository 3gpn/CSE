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
        print("You write in %s." % self.name)

    def take_damage(self):
        if self.health == 0:
            print("You destroyed the %s and the soul of Voldemort inside of it." % self.name)


class Cup(Item):
    def __init__(self, description):
        super(Cup, self).__init__("The Cup of Helga Hufflepuff", description)
        self.health = 50

    def take_damage(self):
        if self.health == 0:
            print("You destroyed the %s and the soul of Voldemort inside of it." % self.name)


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


class PortKey(Item):
    def __init__(self, name, description):
        super(PortKey, self).__init__(name, description)

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
        self.defense = ['Asendio', 'Expelliarmus', 'Avada Kedavra', 'Sectumsempra', 'Stupefy',
                      'Expecto Patronum', 'Obliviate', 'Protego']
        self.spell = ['Wingardium Leviosa''Alohamora', 'Lumos', 'Nox']

    def attack(self):
        offense = random.randint(1, 10)
        distance = random.randint(1, 100)
        spell = input("Pick a spell: %s" % self.defense)
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
        super(Club, self).__init__("The Troll's Club", description, '100', '10')

    def attack(self):
        offense = random.randint(1, 10)
        distance = random.randint(1, 20)
        if offense >= 5 and distance <= 10:
            print("You charge at your opponent and swing your %s toward them" % self.name)
        elif distance > 10:
            print("Your opponent is too far away. Move toward them with caution.")
        elif offense == 10 and distance <= 10:
            print("You hit your opponent in the head. They are dead.")
        else:
            print("Your opponent dodged your attack. They are now angered.")


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


class FriedChicken(Consumable):
    def __init__(self, description):
        super(FriedChicken, self).__init__("Ron's Fried Chicken", description)
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
        print("You pour the %s onto your wounds. You gain 75 health points." % self.name)


class HealingPotion(Potion):
    def __init__(self, description):
        super(HealingPotion, self).__init__("Healing Potion", description)
        self.health = 50

    def drink(self):
        print("You pour the %s into your mouth. You gain 50 health points." % self.name)


class LuckyPotion(Potion):
    def __init__(self, description):
        super(LuckyPotion, self).__init__("Felix Felicis", description)
        self.time = 144

    def drink(self):
        print("You pour the %s into your mouth and gain 24 hours of luck." % self.name)


class ImpersonatingPotion(Potion):
    def __init__(self, description):
        super(ImpersonatingPotion, self).__init__("Polyjuice Potion", description)
        self.time = 60

    def drink(self):
        person = input("Choose a Harry Potter character to impersonate.")
        print("You pour the %s into your mouth. You now look like %s." % (self.name, person))


class Clothing(Item):
    def __init__(self, name, description):
        super(Clothing, self).__init__(name, description)
        self.use = False

    def wear(self):
        self.use = True
        print("You put %s on." % self.name)


class Tiara(Clothing):
    def __init__(self, description):
        super(Tiara, self).__init__("Ravenclaw Diadem", description)
        self.health = 50

    def take_damage(self):
        if self.health == 0:
            print("You destroyed the %s and the soul of Voldemort inside of it." % self.name)


class Cloak(Clothing):
    def __init__(self, description):
        super(Cloak, self).__init__("Invisibility Cloak", description)
        self.strength = 1000

    def wear(self):
        print("You completely cover yourself with the %s and are now invisible to those around you." % self.name)

    def take_damage(self):
        self.strength = self.strength - 5
        print("You were hit by something in the distance. You know have %d protection from the "
              "%s." % (self.strength, self.name))


class Accessory(Clothing):
    def __init__(self, name, description, health):
        super(Accessory, self).__init__(name, description)
        self.health = health

    def take_damage(self):
        if self.health == 0:
            print("You destroyed the %s and the soul of Voldemort inside of it." % self.name)


class Locket(Accessory):
    def __init__(self, description, dialogue):
        super(Locket, self).__init__("Slytherin Locket", description, 100)
        self.nightmare = dialogue

    def wear(self):
        print("You place the %s around your neck. Be careful though. You don't want to wear it for "
              "too long." % self.name)

    def possessed(self):
        print(self.nightmare)


class Ring(Accessory):
    def __init__(self, description):
        super(Ring, self).__init__("Marvolo Family Ring", description, 75)

    def wear(self):
        print("You place the %s on your finger." % self.name)
