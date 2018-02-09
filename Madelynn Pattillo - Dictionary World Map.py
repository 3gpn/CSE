# Example:
world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of the white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "You are north of the white house",
        'PATHS': {
            'SOUTH': 'WESTHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert description here",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    }
}

Hogwarts_Campus = {
    'CHAMBER': {
        'NAME': "Chamber of Secrets",
        'DESCRIPTION': "You are in a long, dark chamber deep below the castle with snakes etched on the walls. "
                       "There is a tunnel leading up.",
        'PATHS': {
            'UP': 'BATHROOM'
        }
    },
    'DUNGEONS': {
        'NAME': "The Dungeons",
        'DESCRIPTION': "You are in a large, dark room below the castle. There are doors to the East and West and "
                       "a staircase leading up.",
        'PATHS': {
            'WEST': 'POTIONS',
            'EAST': 'SLYTHERIN',
            'UP': 'LEVEL 1'
        }
    },
    'POTIONS': {
        'NAME': "Potion's Classroom",
        'DESCRIPTION': "You are in one of the bigger dngeons below the castle that is full of desks with couldrons on "
                       "top. There are doors to the East and West.",
        'PATHS': {
            'WEST': 'SNAPE',
            'EAST': 'DUNGEONS'
        }
    },
    'SNAPE': {
        'NAME': "Snape's Office",
        'DESCRIPTION': "You are in a small, dark room adjacent to the Potion's Classroom that has many glass jars "
                       "lining the walls. There is a door to the East.",
        'PATHS': {
            'EAST': 'POTIONS'
        }
    },
    'SLYTHERIN': {
        'NAME': "Slytherin Common Room",
        'DESCRIPTION': "You are in the living quarters of the Slytherins of Hogwarts. There is a door to the West.",
        'PATHS': {
            'WEST': 'DUNGEONS'
        }
    },
    'LEVEL 1': {
        'NAME': "Level 1 Corridor",
        'DESCRIPTION': "You are in a long hallway with doors to the East and West and a staircase leading up.",
        'PATHS': {
            'WEST': 'LIBRARY',
            'EAST': 'ENTRANCE',
            'UP': 'LEVEL 2'
        }
    },
    'LIBRARY': {
        'NAME': "Library",
        'DESCRIPTION': "You are in a large room full of many desks and bookshelves. There is a section of books blocked"
                       " off. There are doors to the East and West.",
        'PATHS': {
            'WEST': 'CLASSROOM 1B',
            'EAST': 'LEVEL 1'
        }
    },
    'CLASSROOM 1B': {
        'NAME': "Transfiguration Classroom",
        'DESCRIPTION': "You are in a spacious rom full of may desks. There is a door to the East.",
        'PATHS': {
            'EAST': 'LIBRARY'
        }
    },
    'ENTRANCE': {
        'NAME': "Entrance Hall",
        'DESCRIPTION': "You are in a big, circular room with tall walls and doorways to the East and West and a door"
                       "to the North.",
        'PATHS': {
            'WEST': 'LEVEL 1',
            'EAST': 'TAPESTRY',
            'NORTH': 'GREAT HALL'
        }
    },
    'GREAT HALL': {
        'NAME': "Great Hall",
        'DESCRIPTION': "You are in an enormous room with 4 long, vertical tables filling the room and 1 long table "
                       "running parallel against the North wall. There is a door to the South.",
        'PATHS': {
            'SOUTH': 'ENTRANCE'
        }
    },
    'TAPESTRY': {
        'NAME': "Tapestry Corridor",
        'DESCRIPTION': "You are in a long hallway whose walls are covered with many tapestries and moving portraits."
                       "There is a door to the East and West.",
        'PATHS': {
            'WEST': 'ENTRANCE',
            'EAST': 'STORAGE'
        }
    },
    'STORAGE': {
        'NAME': "Snape's Storage",
        'DESCRIPTION': "You are in a small room with shelves on every wall that contain viles and jars of unknown "
                       "substances. There is a door at the West side.",
        'PATHS': {
            'WEST': 'TAPESTRY'
        }
    },
    'LEVEL 2': {
        'NAME': "Level 2 Corridor",
        'DESCRIPTION': "You are in a long hallway with doors to the East, North East, and West. There are staircases "
                       "leading up and down.",
        'PATHS': {
            'WEST': 'BATHROOM',
            'EAST': 'RAVENCLAW 1',
            'NORTH EAST': 'HEADMASTER',
            'UP': 'LEVEL 3',
            'DOWN': 'LEVEL 1'
        }
    },
    'BATHROOM': {
        'NAME': "Moaning Myrtle's Bathroom",
        'DESCRIPTION': "You are in a girls' bathroom that's haunted by the ghost of a former student, Myrtle. There is "
                       "a door to the East and a strange snake symbol on one of the sinks...",
        'PATHS': {
            'EAST': 'LEVEL 2',
            'DOWN': 'CHAMBER'
        }
    },
    'RAVENCLAW 1': {
        'NAME': "Ravenclaw Tower",
        'DESCRIPTION': "You are in a tall toer that leads to the living quarters of the Ravenclaws of Hogwarts. There "
                       "is a door to the West and a staircase leading up.",
        'PATHS': {
            'WEST': 'LEVEL 2',
            'UP': 'RAVENCLAW 2'
        }
    },
    'RAVENCLAW 2': {
        'NAME': "Ravenclaw Common Room",
        'DESCRIPTION': "You are in the living quarters of the Ravenclaws of Hogwarts. There is a staircase leading "
                       "down.",
        'PATHS': {
            'DOWN': 'RAVENCLAW 1'
        }
    },
    'HEADMASTER': {
        'NAME': "Headmaster's Tower",
        'DESCRIPTION': "You are in a tall tower with a griffon staircase leading up. There is a door to the South "
                       "West.",
        'PATHS': {
            'UP': 'DUMBLEDORE',
            'SOUTH WEST': 'LEVEL 2'
        }
    },
    'DUMBLEDORE': {
        'NAME': "Dumbledore's Office",
        'DESCRIPTION': "You are in the office of Headmaster Dumbledore which is full of books and portraits of former "
                       "headmasters cover the walls. There is a staircase leading down."
    }
}
