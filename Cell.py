from TileContent import TileContent
from Tile import Tile
from random import randint

class Cell:

    def __init__(self, x:int, y:int):

        self.x = x
        self.y = y
        self.possibilities = [True for c in TileContent]
        self.allowed_count = len(self.possibilities)
        self.collapsed = False

    def update(self, pos:TileContent) -> None:
        if self.collapsed:
            return
        else:
            if self.possibilities[pos]:
                self.allowed_count -= 1
            self.possibilities[pos] = False

    def entropy(self) -> float:
        return len(self.valid_possibilites()) 
    
    def valid_possibilites(self) -> list(bool):
        valid_pos = []

        for i in range(len(self.possibilities)):
            if self.possibilities[i]:
                valid_pos.append(i)

        return valid_pos

    def collapse(self) -> Tile:
        
        valid_idx = self.valid_possibilites()

        selected_content = randint(0, len(valid_idx))

        self.collapsed = True
        self.possibilities = [False for c in TileContent]
        self.possibilities[valid_idx[selected_content]] = True
