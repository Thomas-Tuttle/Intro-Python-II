from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside a Cave Entrance",
                     "North of you, the cave mount beckons"),

    'hallway': Room("Dark Hallway", """A Dark Creepy Hallway"""), 

    'hallway2': Room("Dark Hallway", """Another Dark Creepy Hallway"""),                

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage leads to a doorway to the east. The smell of rotting meat permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'torture': Room("Torture Room", """You see devices used to inflict pain scattered accross the room."""),

    'trap': Room("Trap Door!", """There is no way out!"""),

    'trap2': Room("Trap Door!", """There is no way out!"""),

    'emptyroom': Room("Empty Room", """There are doors in every direction. On the door to the North is an X, to the East and West the doors have a skull on them.  """),

}


# Link rooms together

room['outside'].n_to = room['hallway']

room['hallway'].n_to = room['foyer']
room['hallway'].s_to = room['outside']

room['foyer'].n_to = room['overlook']
room['foyer'].s_to = room['hallway']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].e_to = room['torture']
room['narrow'].w_to = room['foyer']

room['torture'].n_to = room['hallway2']
room['torture'].w_to = room['narrow']

room['hallway2'].n_to = room['emptyroom']
room['hallway2'].s_to = room['torture']

room['emptyroom'].n_to = room['treasure']
room['emptyroom'].s_to = room['hallway2']
room['emptyroom'].e_to = room['trap']
room['emptyroom'].w_to = room['trap2']

room['treasure'].s_to = room['emptyroom']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
       

#
# If the user enters "q", quit the game.
name = input("What is your name? ")
player = Player(name, room['outside'])

print(f"\nHello {player.name}, Its Time to Start Your Journey! \n\nYou Find Yourself {player.currentRoom.name} \n\n{player.currentRoom.description} \n\nControls:\nMove North(n)\nMove South(s)\nMove East(e)\nMove West(w)\nQuit Game(q)")

quit = False

while not quit:
    command = input("\nWhere Will you Go?\n")

    if command == 'n' or command == 'e' or command == 'w' or command == 's':
        print(player.move(command))

    elif command == 'q':
        quit = True
        print('Game Over')

    else:
        print('You Cant Do That!')
