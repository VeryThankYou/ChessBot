from player import *
from piece import *

class Chess:
    def __init__(self):
        self.p1 = Player("w")
        self.p2 = Player("b")
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        officerList = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(8):
            self.grid[0][i] = officerList[i]([i, 0], self.p1)
            self.grid[1][i] = Pawn([i, 1], self.p1)
            self.grid[7][i] = officerList[i]([i, 7], self.p2)
            self.grid[6][i] = Pawn([i, 6], self.p2)
if __name__=="__main__":
    game = Chess()
    print(game.grid)