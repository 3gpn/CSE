class Room(object):
    def __init__(self, name, north, northeast, northwest, south, southeast, southwest, east, west, up, down,
                 description):
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

    def move(self, direction):
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
                    current_node = current_node[directions]
                except KeyError:
                    print("You cannot go this way.")
            else:
                print("Command not Recognized")


# Initialize Rooms
entrance = Room("Entrance Hall", None, None, 'great_hall', None, None, 'courtyard', 'tapestry', 'level_1', None, None,
                "You are in a big, circular room with tall walls and doorways to the East and West and a door to the "
                "North and South.")
classroom_1B = Room("Transfiguration Classroom", None, None, None, None, None, None, 'library', None, None, None, "You "
                    "are in a spacious room full of many desks. There is a door to the East.")
library = Room("Library", None, None, None, None, None, None, 'level_1', 'classroom_1B', None, None, "You are in a "
               "large room full of many desks and bookshelves. There is a section of books blocked off. There are doors"
               " to the East and West.")
level_1 = Room("Level 1 Corridor", None, None, None, None, None, None, 'entrance', 'library', 'level_2', 'dungeons',
               "You are in a long hallway with doors to the East and West and a staircase leading up and down.")
slytherin = Room("Slytherin Common Room", None, None, None, None, None, None, None, 'dungeons', None, None, "You are in"
                 " the living quarters of the Slytherins of Hogwarts. There is a door to the West.")
snape = Room("Snape's Office", None, None, None, None, None, None, 'potions', None, None, None, "You are in a small, "
             "dark room adjacent to the Potion's Classroom that has many glass jars lining the walls. There is a door "
             "to the East.")
potions = Room("Potions Classroom", None, None, None, None, None, None, 'dungeons', 'snape', None, None, "You are in "
               "one of the bigger dungeons below the castle that is full of desks with couldrons on top. There are "
               "doors to the East and West.")
dungeons = Room("The Dungeons", None, None, None, None, None, None, 'slytherin', 'potions', 'level_1', None, "You are "
                "in a large, dark room below the castle. There are doors to the East and West and a staircase leading "
                "up.")
chamber = Room("Chamber of Secrets", None, None, None, None, None, None, None, None, 'bathroom', None, "You are in a "
               "long, dark chamber deep below the castle with snakes etched on the walls. There is a tunnel leading "
               "up.")
hall = Room("Great Hall", None, None, None, 'entrance', None, None, None, None, None, None, "You are in an enormous "
            "room with 4 long, vertical tables filling the room and 1 long table running parallel against the North "
            "wall. There is a door to the South.")
tapestry = Room("Tapestry Corridor", None, None, None, None, None, None, 'storage', 'entrance', None, None, "You are in"
                " a long hallway whose walls are covered with many tapestries and moving portraits. There is a door to "
                "the East and West.")
storage = Room("Snape's Storage", None, None, None, None, None, None, None, 'tapestry', None, None, "You are in a small"
               " room with shelves on every wall that contain viles and jars of unknown substances. There is a door at "
               "the West side.")
level_2 = Room("Level 2 Corridor", None, 'headmaster', None, None, None, None, 'ravenclaw_1', 'bathroom', 'level_3',
               'level_1', "You are in a long hallway with doors to the East, Northeast, and West. There are staircases "
                          "leading up and down.")
bathroom = Room("Moaning Myrtle's Bathroom", None, None, None, None, None, None, 'level_2', None, None, None, "You are "
                "in a girls' bathroom that's haunted by the ghost of a former student, Myrtle. There is a door to the "
                "East and a strange snake symbol on one of the sinks...")
ravenclaw_1 = Room("Ravenclaw Tower", None, None, None, None, None, None, None, 'level_2', 'ravenclaw_2', None, "You "
                   "are in a tall tower that leads to the living quarters of the Ravenclaws of Hogwarts. There is a "
                   "doorway to the West and a staircase leading up.")
ravenclaw_2 = Room("Ravenclaw Common Room", None, None, None, None, None, None, None, None, None, 'ravenclaw_1', "You "
                   "are in the living quarters of the Ravenclaws of Hogwarts. There is a staircase leading down.")
headmaster = Room("Headmaster's Tower", None, None, None, None, None, 'level_1', None, None, 'dumbledore', None, "You "
                  "are in a tall tower with a griffon staircase leading up. There is a door to the Southwest.")
dumbledore = Room("Dumbledore's Office", None, None, None, None, None, None, None, None, None, 'headmaster', "You are "
                  "in the office of Headmaster Dumbledore which is full of books and portraits of former headmasters "
                  "cover the walls. There is a staircase leading down.")
level_3 = Room("Level 3 Corridor", None, None, 'gryffindor_1', None, None, None, None, 'fluffy', 'level_4', 'level_2',
               "You are in a long hallway with a door to the West and Northwest and staircases leading up and down.")
fluffy = Room("Fluffy's Room", None, None, None, None, None, None, 'level_3', None, None, None, "You are in a large, "
              "dark room that is guarded by a giant three-headed dog named Fluffy. There is a trapdoor at the center of"
              " the room and a door to the East.")
gryffindor_1 = Room("Gryffindor Tower", 'gryffindor_2', None, None, None, 'level_3', None, None, None, None, None, "You"
                    " are in a tall tower that leads to the living quarters of the Gryffindors of Hogwarts. There is a "
                    "painting of the Fat Lady and doors to the North and Southeast.")
gryffindor_2 = Room("Gryffindor Common Room", None, None, None, 'gryffindor_1', None, None, None, None, None, None,
                    "You are in the living quarters of the Gryffindors of Hogwarts. There is a door to the South.")
level_4 = Room("Level 4 Corridor", None, None, None, None, None, None, None, None, 'level_5', 'level_3', "You are in a "
               "long hallway with stairs leading up and down.")
level_5 = Room("Level 5 Corridor", None, None, None, None, None, None, None, None, 'level_6', 'level_4', "You are in a "
               "long hallway with staircases leading up and down.")
level_6 = Room("Level 6 Corridor", None, None, None, None, None, None, None, None, 'level_7', 'level_5', "You are in a "
               "long hallway with staircases leading up and down.")
level_7 = Room("Level 7 Corridor", None, None, None, None, None, None, 'requirements', None, None, 'level_6', "You are "
               "in a long hallway with a huge tapestry to the East on the North wall. Maybe you should walk up to it..."
               " There is a staircase leading down.")
requirements = Room("Room of Requirements", None, None, None, None, None, None, None, 'level_7', None, None, "You are "
                    "in a magical room that constantly changes depending on the needs of those looking for it. Right "
                    "now, it is a large room with piles of random items. There is a door to the West.")
courtyard = Room("Main Courtyard", 'entrance', 'quidditch_field', 'hogsmeade', None, 'willow_tree', None, 'forrest',
                 'lake', None, None, "You are in a large, open space in front of the Entrance Hall outside the castle. "
                                     "There is a path to the West, Northwest, North, Northeast, East, and Southeast.")
forrest = Room("The Forbidden Forrest", None, None, None, None, None, None, None, 'courtyard', None, None, "You are in "
               "a dark, mysterious forest located to the East of the castle. It is off limits to the students due to "
               "the deadly creature that live in here so beware. There is a path to the West.")
willow_tree = Room("The Whomping Willow", None, None, 'courtyard', None, None, None, None, None, None, None, "You are "
                   "standing a few feet from the Whomping Willow, a tall Willow tree that has been a resident at "
                   "Hogwarts for over 70 years and has a nasty temper. Watch out for that tree branch!")
quidditch_field = Room("The Quidditch Field", None, None, None, None, None, 'courtyard', None, None, None, None, "You "
                       "are standing on a grassy, rectangular field that is surrounded by tall stands and four towers, "
                       "each one the color of a Hogwarts House. There are 3 hoops on the East and West side and a path "
                       "to the Southwest.")
hogsmeade = Room("Hogsmeade", 'shack', None, None, None, 'couryard', None, None, None, None, None, "You are standing on"
                 " a long street that has buildings lining both its sides. There are many Hogwarts students covering "
                 "the streets and filling the shops. There is a path to the North and Southeast.")
lake = Room("The Black Lake", None, None, None, None, None, None, 'courtyard', None, None, None, "You are standing on "
            "the bank of a large lake that sits next to Hogwarts. It has dark, murky water with mysterious creatures "
            "lurking below the surface. There is a path to the East.")
shack = Room("The Shrieking Shack", None, None, None, 'hogsmeade', None, None, None, None, None, None, "You are "
             "standing at the gates of a mysterious, boarded up shack. It is feared by most. There is a path to the "
             "South.")
room = Room("Inside the Shrieking Shack", None, None, None, None, None, None, None, None, 'willow_tree', None, "You are"
            " inside the Shrieking Shack in a small, dusty room. There is a passage leading up behind you.")
