import sys

class Life(object):

    def __init__(self, state=None):
        #set the board state or create an empty board
        if state != None:
            self.board = state
        else:
            print('No init state, creating empty 3x3 board')
            self.board = [[False for r in range(3)] for c in range(3)]
    
    def get_alive_neighbours(self, pos):
        r, c = pos
        neighbour_locations = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                               (r, c - 1),                 (r, c + 1),
                               (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
        count = 0
        for r, c in neighbour_locations:
            try:
                if self.board[r][c] == True:
                    count += 1
            except IndexError as e:
                pass
        
        return count

	#def evolve(self, state):
    
