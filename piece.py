
class Piece:
    def __init__(self, position, player):
        self.position = position
        self.player = player
        self.hasmoved = False

    

class Pawn(Piece):
    def isMoveLegal(self, newPos):
        if self.player.color == "w":
            if newPos[1] == self.position[1] + 1 and newPos[0] == self.position[0]:
                return True
        else:
            if newPos[1] == self.position[1] - 1 and newPos[0] == self.position[0]:
                return True
        return False


class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

if __name__=="__main__":
    pawn = Pawn([3, 4])
    print(pawn.position)