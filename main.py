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
    
    def printBoard(self):
        # evt gøre pæn
        printGrid = self.grid.copy()
        printGrid.reverse()
        for row in printGrid:
            for e in row:
                print(e, end=" ")
            print("")

    def play(self):
        # While loop that runs as long as the game isn't over
        # let's each player do a move command
        pass

    def isCheck(self):
        # Checks if the position is in check. Maybe return the player who is in check if any.
        # Maybe give a grid as parameter, so it can be checked for hypothetical states.
        pass

if __name__=="__main__":
    game = Chess()
    game.printBoard()
