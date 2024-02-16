
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
    # Mangler del om har rykket eller ej 


class Knight(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0])> 0 and abs(newPos[1]-self.position[1])> 0 and abs(newPos[0]-self.position[0]) + abs(newPos[1]-self.position[1]) == 3: 
            return True 
        return False 


class Bishop(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0]) == abs(newPos[1]-self.position[1]):
            return True
        return False 

class Rook(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0]) == 0 and abs(newPos[1]-self.position[1])>0 or abs(newPos[1]-self.position[1]) == 0 and abs(newPos[0]-self.position[0])>0:
            # Jeg er lidt i tvivl om 'or' kan bruges her ordentligt 
            return True 
        # Mangler del om har rykket eller ej 

class Queen(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0]) == abs(newPos[1]-self.position[1]) or abs(newPos[0]-self.position[0]) == 0 and abs(newPos[1]-self.position[1])>0 or abs(newPos[1]-self.position[1]) == 0 and abs(newPos[0]-self.position[0])>0:
            # Er igen lidt i tvivl om 'or' er korrekt 
            return True

class King(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0]) == 1 and abs(newPos[1]-self.position[1]) == 1 or abs(newPos[0]-self.position[0]) == 0 and abs(newPos[1]-self.position[1]) == 1 or abs(newPos[0]-self.position[0]) == 1 and abs(newPos[1]-self.position[1]) == 0:
            return True 

if __name__=="__main__":
    pawn = Pawn([3, 4])
    print(pawn.position)