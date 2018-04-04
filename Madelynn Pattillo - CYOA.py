import random


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def view(self):
        print(self.description)

    def hold(self):
        print("You put %s in your inventory." % self.name)

    def take(self):
        print("You place the %s in your inventory." % self.name)


class Diary(Item):
    def __init__(self, description, pages):
        super(Diary, self).__init__("The Diary of Tom M. Riddle", description)
        self.pages = pages
        self.health = 100

    def read(self):
        print("You open the Diary. It says,")
        print(self.pages)

    def talk(self):
        words = input("What would you like to put in the journal?")
        print("You write %s in %s." % (words, self.name))

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
                        'Expecto Patronum', 'Obliviate', 'Protego', 'Incedio', 'Volatilis Lutum (Bat-Bogey Hex)']
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

    def use(self):
        spell = input("Pick a spell: %s" % self.spell)
        print("Your wand flickers as you cast the %s charm." % spell)


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
    def __init__(self, description):
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


class PolyjuicePotion(Potion):
    def __init__(self, description):
        super(PolyjuicePotion, self).__init__("Polyjuice Potion", description)
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


class Characters(object):
    def __init__(self, name, description, inventory, dialogue, distance):
        self.name = name
        self.description = description
        self.health = 100
        self.inventory = inventory
        self.dialogue = dialogue
        self.distance = distance

    def talk(self):
        print("Hello, my name is %s" % self.name)
        print(self.dialogue)

    def view(self):
        print(self.description)

    def attack(self):
        offence = random.randint(1, 10)
        while self.health > 0:
            if offence >= 5:
                print("%s attacks their opponent and hits them." % self.name)
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


class Room(object):
    def __init__(self, name, north, northeast, northwest, south, southeast, southwest, east, west, up, down,
                 description, item, character):
        self.name = name
        self.description = description
        self.north = north
        self.northeast = northeast
        self.northwest = northwest
        self.south = south
        self.southeast = southeast
        self.southwest = southwest
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.item = item
        self.character = character


albus = Characters("Headmaster Albus Dumbledore", "Albus is an old man, though no one knows his age, with cresent moon"
                   " shaped spectacles.", 'Ring, Wand', "Welcome to Hogwarts School of Witchcraft and Wizardry!", 10)
basilisk = Characters("The Basilisk", "It is a long, snake like creature that is known for its ability to freeze any "
                      "living creature in its tracks by staring it in the eye. This beast is what is left of Salazar "
                      "Sytherin.", 'empty', "Slth...", 25)
severus = Characters("Professor Severus Snape", "Severus is a professor with a mysterious, troubled soul. For Harry "
                     "Potter's first six years at Hogwarts, he received a great deal of critizism from Professor "
                     "Snape.", 'Wand', "Stay out of my storage and turn to page 394!", 3)
dementor = Characters("Dementor", "A cloaked figure that hovers above the ground. They suck all of the happiness"
                         " out of the world around them.", 'empty', "Aaaaaa...", 40)
phoenix = Characters("Fawkes", "Flamed colored phoenix that is the loyal companion of Dumbledore. His tears can be used"
                     " as a means of healing.", 'Tear', "Rrraaawwwkkk", 5)
dog = Characters("Fluffy", "Fluffy is the ginormous three-headed dog of Hagrid. His job is to guard that trapdoor.",
                 'empty', "Grrrr", 10)
moaning_myrtle = Characters("Moaning Myrtle", "Moaning Myrtle is the ghost of a past Hogwarts student that haunts the "
                            "girls' bathroom on the second floor.", 'empty', "Hello, who might you be, ha huh?", 5)
cat = Characters("Mrs. Norris", "Mrs. Norris is the beloved cat of Argus Filch, the caretaker of Hogwarts School. Don't"
                 "be caught by her or Filch after hours.", 'empty', "Meow", 20)
filch = Characters("Argus Filch", "Argus Filch is the caretaker of Hogwarts School of Witchcraft and Wizardry. He is a"
                   "nasty old man who loves to catch students wandering the halls after hours.", 'empty', "What are you"
                   "doing out of bed after hours!?", 20)
voldemort = Characters("Lord Voldemort", "A man who looks strangely snake-like. His goal is to spread terror through "
                       "the Wizarding World and rid the world of Harry Potter who will defeat him.", 'Wand', "Harry "
                       "Potter, the boy who will die at my hands!", 40)
harry = Characters("Harry Potter", "Harry Potter is the famous 'Boy Who Lived'. He survived the Killing Curse aimed at "
                   "him by Voldemort. The job of defeating Lord Voldemort was bestowed on him since age 1", 'Wand',
                   "These are my friends, Hermione Granger and Ron Weasley.", 5)
hermione = Characters("Hermione Granger", "Hermione Granger is the brightest witch in her class. She is best friends "
                      "with Ron Weasley and the famous Harry Potter.", 'Wand', "Hello. Would you help us defeat Lord"
                      " Voldemort? We need to find a list of items and destroy them in order to defeat him.", 5)
ron = Characters("Ron Weasley", "Ron Weasley is the youngest son of the famously large, red-headed Weasley family. He "
                                "is best friends with Hermione Granger and the famous Harry Potter.", 'Wand', "We "
                                "really could use the help.", 5)
neville = Characters("Neville Longbottom", "Neville is a Gryffindor student most known for being clumsy yet very good "
                     "at Herbology.", 'Wand', "Hello, I'm Neville. Have you seen Trevor? He's my toad.", 5)
mcgonagall = Characters("Professor Minerva Mcgonagall", "Professor Mcgonagall is the Transfiguration teacher at Hogwarts"
                                                        "and is know for her ability to turn into a cat. She wears "
                                                        "spectacles and a gray witch hat.", 'Wand', "Hello, welcome to"
                                                        "Hogwarts.", 5)
peter = Characters("Peter Petigrew", "Peter is a small, rat like man. He is a follower of Voldemort.", 'empty', "Show"
                                     "me mercy, please, Mr. Potter. ", 5)
draco = Characters("Draco Malfoy", "Draco is a platinum blonde Slytherin who comes from the well known pure-blood "
                                   "family: the Malfoys.", 'Wand', "Get out of herer you filthy Mudblood!", 5)
Lucius = Characters("Lucius Malfoy", "Lucius is a platinum blonde like his son, Draco, and is known for his arrogance.",
                    'Wand', "What do we have here, a filthy Mudblood.", 5)

entrance = Room("Entrance Hall", None, None, 'great_hall', None, None, 'courtyard', 'tapestry', 'level_1', None, None,
                "You are in a big, circular room with tall walls and doorways to the East and West and a door to the "
                "North and South.", None, 'neville')
classroom_1B = Room("Transfiguration Classroom", None, None, None, None, None, None, 'library', None, None, None, "You "
                    "are in a spacious room full of many desks. There is a door to the East.", 'Cup', 'mcgonagall')
library = Room("Library", None, None, None, None, None, None, 'level_1', 'classroom_1B', None, None, "You are in a "
               "large room full of many desks and bookshelves. There is a section of books blocked off. There are doors"
               " to the East and West.", 'Book', 'filch, cat')
level_1 = Room("Level 1 Corridor", None, None, None, None, None, None, 'entrance', 'library', 'level_2', 'dungeons',
               "You are in a long hallway with doors to the East and West and a staircase leading up and down.", None,
               None)
slytherin = Room("Slytherin Common Room", None, None, None, None, None, None, None, 'dungeons', None, None, "You are in"
                 " the living quarters of the Slytherins of Hogwarts. There is a door to the West.", 'Locket', 'draco')
snape = Room("Snape's Office", None, None, None, None, None, None, 'potions', None, None, None, "You are in a small, "
             "dark room adjacent to the Potion's Classroom that has many glass jars lining the walls. There is a door "
             "to the East.", 'HealingPotion', None)
potions = Room("Potions Classroom", None, None, None, None, None, None, 'dungeons', 'snape', None, None, "You are in "
               "one of the bigger dungeons below the castle that is full of desks with couldrons on top. There are "
               "doors to the East and West.", None, 'severus')
dungeons = Room("The Dungeons", None, None, None, None, None, None, 'slytherin', 'potions', 'level_1', None, "You are "
                "in a large, dark room below the castle. There are doors to the East and West and a staircase leading "
                "up.", 'Key', None)
chamber = Room("Chamber of Secrets", None, None, None, None, None, None, None, None, 'bathroom', None, "You are in a "
               "long, dark chamber deep below the castle with snakes etched on the walls. There is a tunnel leading "
               "up.", 'Diary', 'basilisk')
hall = Room("Great Hall", None, None, None, 'entrance', None, None, None, None, None, None, "You are in an enormous "
            "room with 4 long, vertical tables filling the room and 1 long table running parallel against the North "
            "wall. There is a door to the South.", 'FriedChicken', 'albus')
tapestry = Room("Tapestry Corridor", None, None, None, None, None, None, 'storage', 'entrance', None, None, "You are in"
                " a long hallway whose walls are covered with many tapestries and moving portraits. There is a door to "
                "the East and West.", None, None)
storage = Room("Snape's Storage", None, None, None, None, None, None, None, 'tapestry', None, None, "You are in a small"
               " room with shelves on every wall that contain viles and jars of unknown substances. There is a door at "
               "the West side.", 'Gillyweed', None)
level_2 = Room("Level 2 Corridor", None, 'headmaster', None, None, None, None, 'ravenclaw_1', 'bathroom', 'level_3',
               'level_1', "You are in a long hallway with doors to the East, Northeast, and West. There are staircases "
                          "leading up and down.", None, None)
bathroom = Room("Moaning Myrtle's Bathroom", None, None, None, None, None, None, 'level_2', None, None, None, "You are "
                "in a girls' bathroom that's haunted by the ghost of a former student, Myrtle. There is a door to the "
                "East and a strange snake symbol on one of the sinks...", 'ImpersonatingPotion', 'moaning_myrtle')
ravenclaw_1 = Room("Ravenclaw Tower", None, None, None, None, None, None, None, 'level_2', 'ravenclaw_2', None, "You "
                   "are in a tall tower that leads to the living quarters of the Ravenclaws of Hogwarts. There is a "
                   "doorway to the West and a staircase leading up.", None, None)
ravenclaw_2 = Room("Ravenclaw Common Room", None, None, None, None, None, None, None, None, None, 'ravenclaw_1', "You "
                   "are in the living quarters of the Ravenclaws of Hogwarts. There is a staircase leading down.", None,
                   None)
headmaster = Room("Headmaster's Tower", None, None, None, None, None, 'level_1', None, None, 'dumbledore', None, "You "
                  "are in a tall tower with a griffon staircase leading up. There is a door to the Southwest.", None,
                  None)
dumbledore = Room("Dumbledore's Office", None, None, None, None, None, None, None, None, None, 'headmaster', "You are "
                  "in the office of Headmaster Dumbledore which is full of books and portraits of former headmasters "
                  "cover the walls. There is a staircase leading down.", None, 'phoenix')
level_3 = Room("Level 3 Corridor", None, None, 'gryffindor_1', None, None, None, None, 'fluffy', 'level_4', 'level_2',
               "You are in a long hallway with a door to the West and Northwest and staircases leading up and down.",
               None, None)
fluffy = Room("Fluffy's Room", None, None, None, None, None, None, 'level_3', None, None, None, "You are in a large, "
              "dark room that is guarded by a giant three-headed dog named Fluffy. There is a trapdoor at the center of"
              " the room and a door to the East.", None, 'dog')
gryffindor_1 = Room("Gryffindor Tower", 'gryffindor_2', None, None, None, 'level_3', None, None, None, None, None, "You"
                    " are in a tall tower that leads to the living quarters of the Gryffindors of Hogwarts. There is a "
                    "painting of the Fat Lady and doors to the North and Southeast.", None, None)
gryffindor_2 = Room("Gryffindor Common Room", None, None, None, 'gryffindor_1', None, None, None, None, None, None,
                    "You are in the living quarters of the Gryffindors of Hogwarts. There is a door to the South.",
                    'Cloak', 'harry, hermione, ron')
level_4 = Room("Level 4 Corridor", None, None, None, None, None, None, None, None, 'level_5', 'level_3', "You are in a "
               "long hallway with stairs leading up and down.", None, None)
level_5 = Room("Level 5 Corridor", None, None, None, None, None, None, None, None, 'level_6', 'level_4', "You are in a "
               "long hallway with staircases leading up and down.", None, None)
level_6 = Room("Level 6 Corridor", None, None, None, None, None, None, None, None, 'level_7', 'level_5', "You are in a "
               "long hallway with staircases leading up and down.", None, None)
level_7 = Room("Level 7 Corridor", None, None, None, None, None, None, 'requirements', None, None, 'level_6', "You are "
               "in a long hallway with a huge tapestry to the East on the North wall. Maybe you should walk up to it..."
               " There is a staircase leading down.", None, None)
requirements = Room("Room of Requirements", None, None, None, None, None, None, None, 'level_7', None, None, "You are "
                    "in a magical room that constantly changes depending on the needs of those looking for it. Right "
                    "now, it is a large room with piles of random items. There is a door to the West.", 'Tiara', None)
courtyard = Room("Main Courtyard", 'entrance', 'quidditch_field', 'hogsmeade', None, 'willow_tree', None, 'forrest',
                 'lake', None, None, "You are in a large, open space in front of the Entrance Hall outside the castle. "
                                     "There is a path to the West, Northwest, North, Northeast, East, and Southeast.",
                 None, 'dementor')
forrest = Room("The Forbidden Forrest", None, None, None, None, None, None, None, 'courtyard', None, None, "You are in "
               "a dark, mysterious forest located to the East of the castle. It is off limits to the students due to "
               "the deadly creature that live in here so beware. There is a path to the West.", None, None)
willow_tree = Room("The Whomping Willow", None, None, 'courtyard', None, None, None, None, None, None, None, "You are "
                   "standing a few feet from the Whomping Willow, a tall Willow tree that has been a resident at "
                   "Hogwarts for over 70 years and has a nasty temper. Watch out for that tree branch!", None, None)
quidditch_field = Room("The Quidditch Field", None, None, None, None, None, 'courtyard', None, None, None, None, "You "
                       "are standing on a grassy, rectangular field that is surrounded by tall stands and four towers, "
                       "each one the color of a Hogwarts House. There are 3 hoops on the East and West side and a path "
                       "to the Southwest.", 'Snitch', 'dementor')
hogsmeade = Room("Hogsmeade", 'shack', None, None, None, 'couryard', None, None, None, None, None, "You are standing on"
                 " a long street that has buildings lining both its sides. There are many Hogwarts students covering "
                 "the streets and filling the shops. There is a path to the North and Southeast.", None, None)
lake = Room("The Black Lake", None, None, None, None, None, None, 'courtyard', None, None, None, "You are standing on "
            "the bank of a large lake that sits next to Hogwarts. It has dark, murky water with mysterious creatures "
            "lurking below the surface. There is a path to the East.", None, 'dementor')
shack = Room("The Shrieking Shack", None, None, None, 'hogsmeade', None, None, None, None, None, None, "You are "
             "standing at the gates of a mysterious, boarded up shack. It is feared by most. There is a path to the "
             "South.", None, None)
room = Room("Inside the Shrieking Shack", None, None, None, None, None, None, None, None, 'willow_tree', None, "You are"
            " inside the Shrieking Shack in a small, dusty room. There is a passage leading up behind you.", None, None)
maze = Room("The Maze", None, None, None, None, None, None, None, None, None, None, "You are standing on the Quidditch"
                                                                                    "Field after Dumbledore turned it "
                                                                                    "into the maze for the Triwizard "
                                                                                    "Tournament.", 'PortKey', None)
grave = Room("Graveyard", None, None, None, None, None, None, None, None, None, None, "The portkey brought you to a "
             "dark, misty graveyard. There is a tall, cloaked figure in the distance.", 'Portkey', 'voldemort, harry '
             'potter, lucius, peter')

global current_node
        current_node = globals()[getattr(self, direction)]
        current_node = courtyard
        directions = ['north', 'northwest', 'northeast', 'west', 'east', 'south', 'southwest', 'southeast', 'up',
                      'down']
        short_directions = ['n', 'nw', 'ne', 'w', 'e', 's', 'sw', 'se', 'u', 'd']
        while True:
            print(current_node.name)
            print(current_node.description)
            command = input('>_').lower()
            if command == 'quit':
                quit(0)
            elif command in short_directions:
                pos = short_directions.index(command)
                command = directions[pos]
            if command in direction:
                try:
                    current_node.move(command)
                except KeyError:
                    print("You cannot go this way.")
            else:
                print("Command not Recognized")
