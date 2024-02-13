
class Chess:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]


if __name__=="__main__":
    game = Chess()
    print(game.grid)