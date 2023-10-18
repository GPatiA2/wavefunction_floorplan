from TileContent import TileContent
from PyQt5.QtWidgets import *
from random import randint
from typing import Mapping
import numpy as np

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

    def collapse(self) -> None:
        
        valid_idx = self.valid_possibilites()

        selected_content = randint(0, len(valid_idx))

        self.possibilities = [False for c in TileContent]
        self.possibilities[valid_idx[selected_content]] = True

        self.collapsed = True

    def collapse_to_value(self, tc:TileContent) -> None:
        self.possibilities = [False for c in TileContent]
        self.possibilities[tc] = True
        self.collapsed = True

    def draw(self, img_collection) -> TileContent:
        if self.collapsed:
            pb = QPushButton("")
            pb.setIcon(img_collection[self.possibilities.index(True)])
            return pb
        else:
            return QPushButton("")