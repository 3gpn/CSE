class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
entrance = Room("Entrance Hall", 'great_hall', 'courtyard', 'tapestry', 'level_1', None, None, "You are in a big, "
                "circular room with tall walls and doorways to the East and West and a door to the North and South.")
classroom_1B = Room("Transfiguration Classroom", None, None, 'library', None, None, None, "You are in a spacious room "
                    "full of many desks. There is a door to the East.")
library = Room("Library", None, None, 'level_1', 'classroom_1B', None, None, "You are in a large room full of many "
               "desks and bookshelves. There is a section of books blocked off. There are doors to the East and West.")
level_1 = Room("Level 1 Corridor", None, None, 'entrance', 'library', 'level_2', 'dungeons', "You are in a long hallway"
               " with doors to the East and West and a staircase leading up and down.")
slytherin = Room("Slytherin Common Room", None, None, None, 'dungeons', None, None, "You are in the living quarters of "
                 "the Slytherins of Hogwarts. There is a door to the West.")
snape = Room("Snape's Office", None, None, 'potions', None, None, None, "You are in a small, dark room adjacent to the "
             "Potion's Classroom that has many glass jars lining the walls. There is a door to the East.")
potions = Room("Potions Classroom", None, None, 'dungeons', 'snape', None, None, "You are in one of the bigger dungeons"
               " below the castle that is full of desks with couldrons on top. There are doors to the East and West.")
dungeons = Room("The Dungeons", None, None, 'slytherin', 'potions', 'level_1', None, "You are in a large, dark room "
                "below the castle. There are doors to the East and West and a staircase leading up.")
