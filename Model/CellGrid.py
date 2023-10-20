from Model.Cell import Cell
from Model.Exceptions import OutOfBoundsException
from Model.TileContent import TileContent
from Model.GridObserver import GridObserver
from typing import TypeAlias
from Model.AdjacencyRule import AdjacencyRule
from Model.TileContent import Side

ObserverList : TypeAlias = list[GridObserver]

class CellGrid:

    ADJACENCY_COORDS = {
        Side.TOP : (-1, 0),
        Side.RIGHT : (0, 1),
        Side.BOT : (1, 0),
        Side.LEFT : (0, -1)
    }

    def __init__(self, width:int, height:int, adjRules:list[AdjacencyRule]):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(width)] for x in range(height)]
        self.notCollapsed = width * height
        self.adjRules = adjRules
        self.observers : ObserverList = []

    def addObserver(self, go:GridObserver) -> None:
        self.observers.append(go)

    def getCell(self, x:int, y:int) -> Cell:
        if x >= 0 and x < self.height and y >= 0 and y < self.width:
            return self.grid[x][y]
        else:
            raise OutOfBoundsException("CellGrid::getCell() - Cell coordinates out of bounds")
        
    def collapseCell(self, x:int, y:int, tc:TileContent) -> None:
        self.grid[x][y].collapse_to_value(tc)
        for go in self.observers:
            go.onCollapse(x, y, tc)
        self.notCollapsed -= 1

    def runAlgorithm(self) -> None:
        
        while self.notCollapsed > 0:
            minEntropyCellCoords = self.getMinEntropyCellCoords()
            minEntropyCell = self.getCell(minEntropyCellCoords[0], minEntropyCellCoords[1])
            minEntropyCell.collapse()
            
            for go in self.observers:
                go.onCollapse(minEntropyCellCoords[0], minEntropyCellCoords[1], minEntropyCell.valid_possibilites()[0])

            self.propagatePerturbation(minEntropyCellCoords[0], minEntropyCellCoords[1], minEntropyCell.valid_possibilites[0])
            self.notCollapsed -= 1

    def getMinEntropyCellCoords(self) -> tuple[int]:

        minEntropy = 1000
        minEntropyCellCoords = None

        for x in range(self.height):
            for y in range(self.width):
                cell = self.getCell(x, y)
                if not cell.collapsed:
                    if cell.entropy() < minEntropy:
                        minEntropy = cell.entropy()
                        minEntropyCellCoords = (x, y)

        return minEntropyCellCoords
    
    def propagatePerturbation(self, x:int, y:int, cc:TileContent) -> None:

        for k, v in self.ADJACENCY_COORDS.items():
            try:
                cell = self.getCell(x + v[0], y + v[1])
                if not cell.collapsed:
                    for rule in filter(lambda x : x.source == cc , self.adjRules):
                        for pos in cell.valid_possibilites():
                            if not rule.checkValid(cc, pos, k):
                                cell.remove_possibility(pos)
            except OutOfBoundsException:
                pass

    