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
        super(Sword, self).__init__("The Sword of Godric Gryffindor", description, 200, 20)

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
        super(Club, self).__init__("The Troll's Club", description, 100, 10)

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


class Tooth(Close):
    def __init__(self, description):
        super(Tooth, self).__init__("Basilisk Tooth", description, 200, 100)

    def attack(self):
        offense = random.randint(1, 10)
        if offense >= 5:
            print("You stab the %s into the item." % self.name)
        else:
            print("You missed.")


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


class Chest(Item):
    def __init__(self, description):
        super(Chest, self).__init__("Chest", description)
        self.lock = True
        self.inventory = ['']

    def unlock(self):
        self.lock = False
        print("You turn the key into the lock of the chest and it opens.")

    def fill(self):
        print("You place the item into the %s. You know have %s inside of it." % (self.name, self.inventory))


class Characters(object):
    def __init__(self, name, description, dialogue):
        self.name = name
        self.description = description
        self.health = 100
        self.inventory = []
        self.dialogue = dialogue
        self.location = None
        self.fight = False

    def talk(self):
        print("Hello, my name is %s" % self.name)
        print(self.dialogue)

    def view(self):
        print(self.description)

    def attack(self):
        offence = random.randint(1, 10)
        if Characters in Room == Enemy:
            self.fight = True
        while self.health > 0 and self.fight == True:
            if offence >= 5:
                print("%s attacks their opponent and hits them." % self.name)
            else:
                print("%s nearly misses their opponent." % self.name)

    def take_damage(self):
        defense = random.randint(1, 10)
        if Characters in Room == Enemy:
            self.fight = True
        while self.health > 0 and self.fight == True:
            if defense <= 5:
                self.health = self.health - 5
                print("%s is hit. They now have %d percent of their health." % (self.name, self.health))
            else:
                print("%s dodges the hit. They have %d percent of their health." % (self.name, self.health))
        if self.health == 0:
            print("%s is dead." % self.name)

    def pick_up(self):
        print("You add the item to your inventory. You know have %s in your inventory." % self.inventory)

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


class Enemy(Characters):
    def __init__(self, name, description, dialogue, distance):
        super(Enemy, self).__init__(name, description, dialogue)
        self. distance = distance
        self.fight = False

    def talk(self):
        print(self.dialogue)

    def attack(self):
        offence = random.randint(1, 10)
        if Characters in Room == Characters:
            self.fight = True
        while self.health > 0 and self.fight == True:
            if offence >= 5:
                print("%s attacks their opponent and hits them." % self.name)
            else:
                print("%s nearly misses their opponent." % self.name)

    def take_damage(self):
        defense = random.randint(1, 10)
        if Characters in Room == Characters:
            self.fight = True
        while self.health > 0 and self.fight == True:
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
        self.characters = character


diary = Diary("This is an old, gray book with gold lettering on the spine that reads Tom M. Riddle.", "Hello, I'm Tom "
              "Marvolo Riddle.")
cup = Cup("This is an old and valuable gold chalice.")
book = Book("History of Hogwarts School of Witchcraft and Wizardry.", "This is a thick, brown book about the history of"
            " the school. It looks like someone marked a page.", "Salazar Slytherin is one of the four founders of "
            "Hogwarts School of Witchcraft and Wizardry. He was know for being a snake tongue and adoring the basilisk."
            " It is said that he dug a series of chambers under the school.")
key = Key("Flying Key", "This is a silver key that has white bird like wings. These wings give it the ability to fly "
          "high above your head.")
snitch = Snitch("This is a small, round golden ball with thin gold wings that move as fast as a hummingbird's. It is "
                "used in the Wizarding game, Quidditch. This particular snitch was caught by Harry Potter during his "
                "first year.")
portkey = PortKey("Triwizard Cup", "This portkey looks exactly like the Triwizard Cup. It will teleport you when you "
                  "touch it.")
wand = Wand("You have a 12 inch oak wand with a phoenix feather core.")
sword = Sword("This sword has a long silver blade with gemstones lining the handle.")
club = Club("This club is a long, round chunk of wood with spikes completely covering it.")
tooth = Tooth("This is a huge, white tooth from the mouth of the basilisk. It is full of poison that can kill anyone in"
              " a matter of seconds.")
gillyweed = Gillyweed("This is a green, slimy plant that looks similar to seaweed. It will allow you to breathe "
                      "underwater for so much time.")
fried_chicken = FriedChicken("This greasy chicken leg is the love of Ron Weasley.")
tear = Tear("This tear is like an average tear, however, it can heal any wound.")
healing_potion = HealingPotion("This is a potion with a pink pigment. It will help keep you alive.")
lucky_potion = LuckyPotion("This is a potion with a yellow pigment. It will give luck in any situation for 24 hours.")
polyjuice_potion = PolyjuicePotion("This is a brown, bubbly potion. It allows you to change your physical appearance "
                                   "into that of another.")
tiara = Tiara("This is a silver diadem with jewels lining the top of it. It was owned by Rowena Ravenclaw, one of the "
              "four Hogwarts founders.")
cloak = Cloak("This is a cloak that changes its appearance to match its surrounding, thus making you invisible to the "
              "human eye.")
locket = Locket("This is a heavy, angular locket on a chain. It contains a portion of Voldemort's soul and must be "
                "destroyed.", "Hhhaaarrryyy Pppooottteeerrr...")
ring = Ring("This is a simple silver ring with the Marvolo family crest engraved into it. It contains a portion of "
            "Voldemort's soul and must be destroyed.")
chest = Chest("This is a small, wooden box big enough to hold five items.")

albus = Characters("Headmaster Albus Dumbledore", "Albus is an old man, though no one knows his age, with crescent moon"
                   " shaped spectacles.", "Welcome to Hogwarts School of Witchcraft and Wizardry!")
basilisk = Enemy("The Basilisk", "It is a long, snake like creature that is known for its ability to freeze any "
                 "living creature in its tracks by staring it in the eye. This beast is what is left of Salazar "
                 "Sytherin.", "Slth...", 25)
severus = Characters("Professor Severus Snape", "Severus is a professor with a mysterious, troubled soul. For Harry "
                     "Potter's first six years at Hogwarts, he received a great deal of criticism from Professor "
                     "Snape.", "Turn to page 394!")
dementor = Enemy("Dementor", "A cloaked figure that hovers above the ground. They suck all of the happiness"
                 " out of the world around them.", "Aaaaaa...", 40)
phoenix = Characters("Fawkes", "Flamed colored phoenix that is the loyal companion of Dumbledore. His tears can be used"
                     " as a means of healing.", "Rrraaawwwkkk")
dog = Characters("Fluffy", "Fluffy is the ginormous three-headed dog of Hagrid. His job is to guard that trapdoor.",
                 "Grrrr")
moaning_myrtle = Characters("Moaning Myrtle", "Moaning Myrtle is the ghost of a past Hogwarts student that haunts the "
                            "girls' bathroom on the second floor.", "Hello, who might you be, ha huh?")
cat = Characters("Mrs. Norris", "Mrs. Norris is the beloved cat of Argus Filch, the caretaker of Hogwarts School. Don't"
                 "be caught by her or Filch after hours.", "Meow")
filch = Characters("Argus Filch", "Argus Filch is the caretaker of Hogwarts School of Witchcraft and Wizardry. He is a"
                   "nasty old man who loves to catch students wandering the halls after hours.", "What are you"
                   "doing out of bed after hours!?")
voldemort = Enemy("Lord Voldemort", "A man who looks strangely snake-like. His goal is to spread terror through "
                  "the Wizarding World and rid the world of Harry Potter who will defeat him.", "Harry "
                  "Potter, the boy who will die at my hands!", 40)
harry = Characters("Harry Potter", "Harry Potter is the famous 'Boy Who Lived'. He survived the Killing Curse casted "
                   "by Voldemort. The job of defeating Lord Voldemort was bestowed on him since age 1", "These are "
                   "my friends, Hermione Granger and Ron Weasley.")
hermione = Characters("Hermione Granger", "Hermione Granger is the brightest witch in her class. She is best friends "
                      "with Ron Weasley and the famous Harry Potter.", "Hello. Would you help us defeat Lord"
                      " Voldemort? We need to find a list of items and destroy them in order to defeat him.")
ron = Characters("Ron Weasley", "Ron Weasley is the youngest son of the famously large, red-headed Weasley family. He "
                 "is best friends with Hermione Granger and the famous Harry Potter.", "We really could use the help.")
neville = Characters("Neville Longbottom", "Neville is a Gryffindor student most known for being clumsy yet very good "
                     "at Herbology.", "Hello, I'm Neville. Have you seen Trevor? He's my toad.")
mcgonagall = Characters("Professor Minerva Mcgonagall", "Professor Mcgonagall is the Transfiguration teacher at "
                        "Hogwarts and is know for her ability to turn into a cat. She wears spectacles and a gray witch"
                        " hat.", "Hello, welcome to Hogwarts.")
peter = Enemy("Peter Pettigrew", "Peter is a small, rat like man. He is a follower of Voldemort.", "Show me mercy, "
              "please, Mr. Potter. ", 5)
draco = Characters("Draco Malfoy", "Draco is a platinum blonde Slytherin who comes from the well known pure-blood "
                   "family: the Malfoys.", "Get out of here you filthy Mudblood!")
lucius = Enemy("Lucius Malfoy", "Lucius is a platinum blonde like his son, Draco, and is known for his arrogance.",
               "What do we have here, a filthy Mudblood.", 5)
nagini = Enemy("Nagini", "Nagini is a large boa constrictor and the dear friend of Voldemort.", None, 8)
ginny = Characters("Ginny Weasley", "Ginny is part of a famous pureblood family, the Weasleys. She has red hair and "
                   "freckles that speckle her face.", "Have you seen an old, gray diary by chance? I need it.")

entrance = Room("Entrance Hall", 'hall', None, None, 'courtyard', None, None, 'tapestry', 'level_1', None, None,
                "You are in a big, circular room with tall walls and doorways to the East and West and a door to the "
                "North and South. Another student stands to the side looking quite distressed.", [], [neville])
classroom_1B = Room("Transfiguration Classroom", None, None, None, None, None, None, 'library', None, None, None, "You "
                    "are in a spacious room full of many desks. There is a door to the East. The professor is sitting "
                    "at her desk, and there is a gold chalice on her desk.", [cup], [mcgonagall])
library = Room("Library", None, None, None, None, None, None, 'level_1', 'classroom_1B', None, None, "You are in a "
               "large room full of many desks and bookshelves. There is a section of books blocked off. There are doors"
               " to the East and West. Argus Filch, the Hogwarts caretaker and his cat scan the library, waiting for a "
               "student to break the rules.", [book], [filch, cat])
level_1 = Room("Level 1 Corridor", None, None, None, None, None, None, 'entrance', 'library', 'level_2', 'dungeons',
               "You are in a long hallway with doors to the East and West and a staircase leading up and down.", [], [])
slytherin = Room("Slytherin Common Room", None, None, None, None, None, None, None, 'dungeons', None, None, "You are in"
                 " the living quarters of the Slytherins of Hogwarts. There is what looks to be a locket laying in a "
                 "corner of the floor, but beware the blonde bully Malfoy. There is a door to the West.", [locket],
                 [draco])
snape = Room("Snape's Office", None, None, None, None, None, None, 'potions', None, None, None, "You are in a small, "
             "dark room adjacent to the Potion's Classroom that has many glass jars lining the walls. There is a pink "
             "healing potion in a black couldron on one of the desks. There is a door to the East.", [healing_potion],
             [])
potions = Room("Potions Classroom", None, None, None, None, None, None, 'dungeons', 'snape', None, None, "You are in "
               "one of the bigger dungeons below the castle that is full of desks with couldrons on top. There are "
               "doors to the East and West. The professor sits at his desk.", [], [severus])
dungeons = Room("The Dungeons", None, None, None, None, None, None, 'slytherin', 'potions', 'level_1', None, "You are "
                "in a large, dark room below the castle. A key shaped figure flies high above your head. There are "
                "doors to the East and West and a staircase leading up.", [key], [])
chamber = Room("Chamber of Secrets", None, None, None, None, None, None, None, None, 'bathroom', None, "You are in a "
               "long, dark chamber deep below the castle with snakes etched on the walls. A long snake with enormous "
               "vangs and eyes as big as beach balls crawls around in the shadows. There is a tunnel leading "
               "up.", [], [basilisk])
hall = Room("Great Hall", None, None, None, 'entrance', None, None, None, None, None, None, "You are in an enormous "
            "room with 4 long, vertical tables filling the room and 1 long table running parallel against the North "
            "wall. There is a door to the South. Headmaster Dumbledore stands at his pedestal waiting to give his "
            "welcoming speech.", [fried_chicken], [albus])
tapestry = Room("Tapestry Corridor", None, None, None, None, None, None, 'storage', 'entrance', None, None, "You are in"
                " a long hallway whose walls are covered with many tapestries and moving portraits. There is a door to "
                "the East and West.", [], [])
storage = Room("Snape's Storage", None, None, None, None, None, None, None, 'tapestry', None, None, "You are in a small"
               " room with shelves on every wall that contain viles and jars of unknown substances. Gillyweed sits up "
               "in a jar on the top shelf. There is a door at the West side.", [gillyweed], [])
level_2 = Room("Level 2 Corridor", None, 'headmaster', None, None, None, None, 'ravenclaw_1', 'bathroom', 'level_3',
               'level_1', "You are in a long hallway with doors to the East, Northeast, and West. There are staircases "
                          "leading up and down.", [], [])
bathroom = Room("Moaning Myrtle's Bathroom", None, None, None, None, None, None, 'level_2', None, None, None, "You are "
                "in a girls' bathroom that's haunted by the ghost of a former student, Myrtle. A gouldron of polyjuice "
                "potion sits in the corner. There is a door to the East and a strange snake symbol on one of the "
                "sinks...", [polyjuice_potion], [moaning_myrtle])
ravenclaw_1 = Room("Ravenclaw Tower", None, None, None, None, None, None, None, 'level_2', 'ravenclaw_2', None, "You "
                   "are in a tall tower that leads to the living quarters of the Ravenclaws of Hogwarts. There is a "
                   "doorway to the West and a staircase leading up.", [], [])
ravenclaw_2 = Room("Ravenclaw Common Room", None, None, None, None, None, None, None, None, None, 'ravenclaw_1', "You "
                   "are in the living quarters of the Ravenclaws of Hogwarts. There is a staircase leading down.", [],
                   [])
headmaster = Room("Headmaster's Tower", None, None, None, None, None, 'level_1', None, None, 'dumbledore', None, "You "
                  "are in a tall tower with a griffon staircase leading up. There is a door to the Southwest.", [],
                  [])
dumbledore = Room("Dumbledore's Office", None, None, None, None, None, None, None, None, None, 'headmaster', "You are "
                  "in the office of Headmaster Dumbledore which is full of books and portraits of former headmasters "
                  "cover the walls. The headmasters loyal pet, Fawkes, sits on his perch on the Headmaster's desk. "
                  "There is a staircase leading down.", [], [phoenix])
level_3 = Room("Level 3 Corridor", None, None, 'gryffindor_1', None, None, None, None, 'fluffy', 'level_4', 'level_2',
               "You are in a long hallway with a door to the West and Northwest and staircases leading up and down.",
               [], [])
fluffy = Room("Fluffy's Room", None, None, None, None, None, None, 'level_3', None, None, None, "You are in a large, "
              "dark room that is guarded by a giant three-headed dog named Fluffy. There is a trapdoor at the center of"
              " the room and a door to the East.", [], [dog])
gryffindor_1 = Room("Gryffindor Tower", 'gryffindor_2', None, None, None, 'level_3', None, None, None, None, None, "You"
                    " are in a tall tower that leads to the living quarters of the Gryffindors of Hogwarts. There is a "
                    "painting of the Fat Lady and doors to the North and Southeast.", [], [])
gryffindor_2 = Room("Gryffindor Common Room", None, None, None, 'gryffindor_1', None, None, None, None, None, None,
                    "You are in the living quarters of the Gryffindors of Hogwarts. The golden-trio: Harry, Ron and "
                    "Hermione sit in a circle talking. Harry is holding a strange cloak, and there is a chest in the "
                    "corner. There is a door to the South.", [cloak, chest], [harry, hermione, ron, ginny])
level_4 = Room("Level 4 Corridor", None, None, None, None, None, None, None, None, 'level_5', 'level_3', "You are in a "
               "long hallway with stairs leading up and down.", [], [])
level_5 = Room("Level 5 Corridor", None, None, None, None, None, None, None, None, 'level_6', 'level_4', "You are in a "
               "long hallway with staircases leading up and down.", [], [])
level_6 = Room("Level 6 Corridor", None, None, None, None, None, None, None, None, 'level_7', 'level_5', "You are in a "
               "long hallway with staircases leading up and down.", [], [])
level_7 = Room("Level 7 Corridor", None, None, None, None, None, None, 'requirements', None, None, 'level_6', "You are "
               "in a long hallway with a huge tapestry to the East on the North wall. Maybe you should walk up to it..."
               " There is a staircase leading down.", [], [])
requirements = Room("Room of Requirements", None, None, None, None, None, None, None, 'level_7', None, None, "You are "
                    "in a magical room that constantly changes depending on the needs of those looking for it. Right "
                    "now, it is a large room with piles of random items. The Ravenclaw Diadem is hidden within these "
                    "walls. There is a door to the West.", [tiara], [])
courtyard = Room("Main Courtyard", 'entrance', 'quidditch_field', 'hogsmeade', None, 'willow_tree', None, 'forrest',
                 'lake', None, None, "You are in a large, open space in front of the Entrance Hall outside the castle. "
                 "There is a path to the West, Northwest, North, Northeast, East, and Southeast.", [], [])
forrest = Room("The Forbidden Forrest", None, None, None, None, None, None, None, 'courtyard', None, None, "You are in "
               "a dark, mysterious forest located to the East of the castle. It is off limits to the students due to "
               "the deadly creature that live in here so beware. There is a path to the West.", [], [])
willow_tree = Room("The Whomping Willow", None, None, 'courtyard', None, None, None, None, None, None, None, "You are "
                   "standing a few feet from the Whomping Willow, a tall Willow tree that has been a resident at "
                   "Hogwarts for over 70 years and has a nasty temper. Watch out for that tree branch!", [], [])
quidditch_field = Room("The Quidditch Field", None, None, None, None, None, 'courtyard', None, None, None, None, "You "
                       "are standing on a grassy, rectangular field that is surrounded by tall stands and four towers, "
                       "each one the color of a Hogwarts House. There are 3 hoops on the East and West side and a path "
                       "to the Southwest. A golden Snitch lies in the center of the field as dementors fly high above "
                       "the field.", [snitch], [dementor])
hogsmeade = Room("Hogsmeade", 'shack', None, None, None, 'couryard', None, None, None, None, None, "You are standing on"
                 " a long street that has buildings lining both its sides. There are many Hogwarts students covering "
                 "the streets and filling the shops. There is a path to the North and Southeast.", [], [])
lake = Room("The Black Lake", None, None, None, None, None, None, 'courtyard', None, None, None, "You are standing on "
            "the bank of a large lake that sits next to Hogwarts. It has dark, murky water with mysterious creatures "
            "lurking below the surface. Dementors fly high above the lake's surface. There is a path to the East.", [],
            [dementor])
shack = Room("The Shrieking Shack", None, None, None, 'hogsmeade', None, None, None, None, None, None, "You are "
             "standing at the gates of a mysterious, boarded up shack. It is feared by most. There is a path to the "
             "South.", [], [])
room = Room("Inside the Shrieking Shack", None, None, None, None, None, None, None, None, 'willow_tree', None, "You are"
            " inside the Shrieking Shack in a small, dusty room. A rat like man, Peter, sits in a corner holding a "
            "silver ring. There is a passage leading up behind you.", [ring], [peter])
maze = Room("The Maze", None, None, None, None, None, None, None, None, None, None,
            "You are standing on the Quidditch Field after Dumbledore turned it into the maze for the Triwizard "
            "Tournament. A portkey lies at the end of the maze.", [portkey], [])
grave = Room("Graveyard", None, None, None, None, None, None, None, None, None, None, "The portkey brought you to a "
             "dark, misty graveyard. There is a tall, cloaked figure in the distance. Harry Potter lies on the ground "
             "holding his right forearm.", [portkey], [voldemort, harry, lucius])

player = Characters("You", "You are a student at Hogwarts School of Witchcraft and Wizardry during the return of "
                    "Lord Voldemort.", None)
player.location = courtyard

if sword in player.inventory:
    gryffindor_2.characters = [hermione]
    dungeons.characters = [ron]
    chamber.item = [diary]
    chamber.characters = [basilisk, harry, ginny]
    harry.dialogue = "Quick, give me the Sword of Godric Gryffindor! I'll take care of the basilisk while you " \
                     "destroy the diary!"
    ginny.description = "She is passed out in the middle of the chamber next to the diary."
    ginny.dialogue = None

if diary.health == 0:
    gryffindor_2.characters = [harry, hermione, ron]
    dungeons.characters = []
    chamber.item = []
    chamber.characters = []
    ginny.description = "Ginny is part of a famous pureblood family, the Weasleys. She has red hair and freckles that" \
                        " speckle her face."
    ginny.dialogue = "Thank you for saving me!"
    harry.dialogue = "These are my friends, Hermione Granger and Ron Weasley."
    courtyard.characters = [dementor]
    courtyard.description = "You are in a large, open space in front of the Entrance Hall outside the castle. Strange" \
                            " cloaked creatures, dementors, float around the courtyard and outside the castle. There " \
                            "is a path to the West, Northwest, North, Northeast, East, and Southeast."
    chest.inventory = [diary]
    player.location = courtyard
    print("You successfully destroyed The Diary of Tom M. Riddle! Its remains are in the chest. You are back at the "
          "courtyard.")

directions = ['north', 'northwest', 'northeast', 'west', 'east', 'south', 'southwest', 'southeast', 'up', 'down']
short_directions = ['n', 'nw', 'ne', 'w', 'e', 's', 'sw', 'se', 'u', 'd']
while True:
    print(player.location.name)
    print(player.location.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command == 'take':
        item = input("What do you want to pick up?")
        if item == portkey and player.location == grave:
            player.location = maze
            print("You were teleported back to the maze at Hogwarts.")
        elif item == portkey and player.location == maze:
            player.location = grave
            print("You were teleported to a graveyard.")
        elif item in Room:
            player.inventory.append(item)
            print("You now have %s in your inventory." % item)
        else:
            print("I'm sorry, but that is not available.")
    elif command == 'place':
        item = input("What do you want to put in the chest?")
        if item in player.inventory:
            player.inventory.remove(item)
            chest.inventory.append(item)
            print("You put %s into the chest." % item)
        else:
            print("I'm sorry, but that is not available.")
    elif command == 'give':
        person = input("Who do you want to give an item?")
        item = input("What do you want to give away?")
        person.inventory = [item]
        if person and item in Room:
            person.inventory.append(item)
            player.inventory.remove(item)
            print("You gave %s the %s." % (person, item))
        else:
            print("I do not understand what you want to do.")
    elif command == 'teleport':
        if chest.inventory == [diary]:
            player.location = maze
            print("You were teleported to a maze.")
        else:
            print("I do not understand what you want.")
    elif command == 'view':
        print(player.location.description)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            player.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not Recognized")
