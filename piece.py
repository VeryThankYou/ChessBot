
class Piece:
    def __init__(self, position, player): # Skal vi her initialisere en piecevalue eller lignende så når vi når til AI'en, så kan vi sætte en værdi på brikkerne? 
        # Ville nok være (1,3,3,5,9) for hhv. bonde, springer, løber osv. og inf/meget høj for kongen
        self.position = position
        self.player = player
        self.hasmoved = False

        # Hvis vi laver init med value: 
        # self.value_sign = 1 if color == "w" else -1 
        # self.value = value*value_sign

    def __str__(self):
        return type(self).__name__ + " " + self.player.color
    

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
        if (abs(newPos[0]-self.position[0]) == 0 and abs(newPos[1]-self.position[1])>0) or (abs(newPos[1]-self.position[1]) == 0 and abs(newPos[0]-self.position[0])>0):
            # Jeg er lidt i tvivl om 'or' kan bruges her ordentligt 
            return True 
        # Mangler del om har rykket eller ej 
        return False

class Queen(Piece):
    def isMoveLegal(self,newPos):
        if (abs(newPos[0]-self.position[0]) == abs(newPos[1]-self.position[1])) or (abs(newPos[0]-self.position[0]) == 0 and abs(newPos[1]-self.position[1])>0) or (abs(newPos[1]-self.position[1]) == 0 and abs(newPos[0]-self.position[0])>0):
            # Er igen lidt i tvivl om 'or' er korrekt 
            return True
        return False

class King(Piece):
    def isMoveLegal(self,newPos):
        if abs(newPos[0]-self.position[0]) <= 1 and abs(newPos[1]-self.position[1]) <= 1:
            return True 
        return False

if __name__=="__main__":
    pawn = Pawn([3, 4])
    print(pawn.position)