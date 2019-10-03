# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.currentRoom = room

    def move(self, direction):
        if direction == 'n' and self.currentRoom.n_to:
            self.currentRoom = self.currentRoom.n_to
            return f'\nYou move North to the {self.currentRoom.name}.\n\n{self.currentRoom.description}'

        elif direction == 's' and self.currentRoom.s_to:
            self.currentRoom = self.currentRoom.s_to
            return f'\nYou move South to the {self.currentRoom.name}.\n\n{self.currentRoom.description}'

        elif direction == 'e' and self.currentRoom.e_to:
            self.currentRoom = self.currentRoom.e_to
            return f'\nYou move East to the {self.currentRoom.name}.\n\n{self.currentRoom.description}'

        elif direction == 'w' and self.currentRoom.w_to:
            self.currentRoom = self.currentRoom.w_to
            return f'\nYou move West to the {self.currentRoom.name}.\n\n{self.currentRoom.description}'

        else:
            return "You can't move that way!"