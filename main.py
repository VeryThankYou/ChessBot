from player import *
from piece import *
"""Grid is indexed as follows:
First dimension is rows where game.grid[0] is row number 1 on a chessboard.
Second dimension is columns where game.grid[0][0] corresponds to a1 on a chessboard"""


class Chess:
    def __init__(self):
        self.p1 = Player("w")
        self.p2 = Player("b")
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.gameOver = False
        officerList = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(8):
            self.grid[0][i] = officerList[i]([i, 0], self.p1)
            self.grid[1][i] = Pawn([i, 1], self.p1)
            self.grid[7][i] = officerList[i]([i, 7], self.p2)
            self.grid[6][i] = Pawn([i, 6], self.p2)

    def getColumn(self, index):
        return [self.grid[i][index] for i in range(8)]
    
    

if __name__=="__main__":
    game = Chess()
    print(game.grid)
