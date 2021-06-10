from random import randint
# This class define the entire game board
# It will be used to create two boards, one for storing what the player sees and one for storing the underlying mines and mine numbers around a given block
# I'm new to classes in python (or anywhere else), so this file will be heavily commented
class Board:

    # This function defines parameters when an instance of the class is created. Here we give it a width and height for the number of positions
    # Later on I will add logic to prevent it from exceeding the terminal window width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['X'] * self.width for _ in range(self.height)]
    
    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.board[i][j], end=' ')
            print('')
        print('')

    def update_board(self, pos_x, pos_y, char):
        self.board[pos_x][pos_y] = char

    def add_mines(self, num_of_mines):
        mines_remaining = num_of_mines
        running = True
        mine = "\033[91mM\033[0m"
        while running:
            for j in range(self.width):
                for k in range(self.height):
                    if mines_remaining == 0:
                        running = False
                    elif self.board[j][k] != mine and randint(1, self.width * self.height) == 1:
                        mines_remaining -= 1
                        self.board[j][k] = mine