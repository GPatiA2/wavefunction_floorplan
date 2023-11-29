from Model.TileContent import TileContent
from PyQt5.QtWidgets import *
from random import randint
from Model.GridObserver import GridObserver
from typing import TypeAlias
ObserverList : TypeAlias = list[GridObserver]

class Cell:

    def __init__(self, x:int, y:int):

        self.x = x
        self.y = y
        self.possibilities = [True for c in TileContent]
        self.allowed_count = len(self.possibilities)
        self.collapsed = False

    def entropy(self) -> float:
        ent = len(self.valid_possibilites()) 
        return ent

    def update_possibilities(self, pos : list[TileContent]):


        
        act_pos = []
        for i in range(len(self.possibilities)):
            if self.possibilities[i]:
                act_pos.append(TileContent(i).name)

        print(" ACTUAL POSSIBILITIES = ", act_pos)

        updating = []
        for i in range(len(pos)):
            if pos[i]:
                updating.append(TileContent(i).name)

        print(" UPDATING WITH = ", updating)

        for idx in range(len(pos)):
            self.possibilities[idx] = self.possibilities[idx] and pos[idx]

        act_pos = []
        for i in range(len(self.possibilities)):
            if self.possibilities[i]:
                act_pos.append(TileContent(i).name)

        print(" NEW ACTUAL POSSIBILITIES = ", act_pos)

    def valid_possibilites(self) -> list[bool]:
        valid_pos = []

        for i in range(len(self.possibilities)):
            if self.possibilities[i]:
                valid_pos.append(i)

        return valid_pos

    def collapse(self) -> None:
        
        valid_idx = self.valid_possibilites()

        selected_content = randint(0, len(valid_idx) - 1) if len(valid_idx) > 1 else 0

        self.possibilities = [False for c in TileContent]
        self.possibilities[valid_idx[selected_content]] = True

        self.collapsed = True

    def collapse_to_value(self, tc:TileContent) -> None:
        self.possibilities = [False for c in TileContent]
        self.possibilities[int(tc)] = True
        self.collapsed = True