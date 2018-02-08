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
        'DESCRIPTION': "You are below the dungeons",
        'PATHS': {
            'UP': 'DUNGEONS'
        }
    },
    'DUNGEONS': {
        'NAME': "The Dungeons",
        'DESCRIPTION': "You are below the castle",
        'PATHS': {
            'WEST': 'POTIONS',
            'EAST': 'SLYTHERIN',
            'UP': 'LEVEL 1'
        }
    },
    'POTIONS': {
        'NAME': "Potion's Classroom",
        'DESCRIPTION': "You are in one of the bigger dungeons below the castle",
        'PATHS': {
            'WEST': 'SNAPE',
            'EAST': 'DUNGEONS'
        }
    },
    'SNAPE': {
        'NAME': "Snape's Office",
        'DESCRIPTION': "You are in a small, dark room adjacent to the Potion's Classroom",
        'PATHS': {
            'EAST': 'POTIONS'
        }
    },
    'SLYTHERIN': {
        'NAME': "Slytherin Common Room",
        'DESCRIPTION': "You are in the living quarters of the Slytherins of Hogwarts"
    }
}
