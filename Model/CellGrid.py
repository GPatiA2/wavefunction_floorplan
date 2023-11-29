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
        self.propagatePerturbation(x,y,tc)
        for go in self.observers:
            go.onCollapse(x, y, tc)
        self.notCollapsed -= 1

    def runAlgorithm(self) -> None:
        
        try:
            while self.notCollapsed > 0:
                print("========================ITERATION========================================")

                minEntropyCellCoords = self.getMinEntropyCellCoords()

                minEntropyCell = self.getCell(minEntropyCellCoords[0], minEntropyCellCoords[1])
                print("COLLAPSING = ", minEntropyCellCoords[0], " ", minEntropyCellCoords[1])
                minEntropyCell.collapse()
                
                for go in self.observers:
                    go.onCollapse(minEntropyCellCoords[0], minEntropyCellCoords[1], minEntropyCell.valid_possibilites()[0])

                self.propagatePerturbation(minEntropyCellCoords[0], minEntropyCellCoords[1], minEntropyCell.valid_possibilites()[0])
                self.notCollapsed -= 1

        except Exception as e :
            print(e)

    def getReciprocalSide(self, side:Side) -> Side:

        if side == Side.TOP:
            return Side.BOT
        elif side == Side.BOT:
            return Side.TOP
        elif side == Side.LEFT:
            return Side.RIGHT
        elif side == Side.RIGHT:
            return Side.LEFT

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
                    print("CELL ", x+v[0], ",", y+v[1])
                    possibilities = [False for it in TileContent]
                    
                    appliable_rules = list(filter(lambda r: r.source == cc and r.side == k, self.adjRules))
                    recip_rules     = list(filter(lambda r: r.dest == cc and r.side == self.getReciprocalSide(k), self.adjRules))

                    ap_rules = []
                    
                    for r in appliable_rules:
                        ap_rules.append("" + TileContent(r.source).name + " " + Side(r.side).name + " " + TileContent(r.dest).name)

                    for r in recip_rules:
                        ap_rules.append("" + TileContent(r.source).name + " " + Side(r.side).name + " " + TileContent(r.dest).name)

                    print(" APPLYING RULES ", ap_rules)

                    for r in appliable_rules:
                        possibilities[r.dest] = True

                    for r in recip_rules:
                        possibilities[r.source] = True
                    
                    if possibilities.count(True) != 0:
                        cell.update_possibilities(possibilities)
                    else:
                        possibilities[TileContent(0)] = True
                        possibilities[TileContent(9)] = True
                        cell.update_possibilities(possibilities)

            except OutOfBoundsException:
                pass

    