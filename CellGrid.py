from Cell import Cell
from Exceptions import OutOfBoundsException
from TileContent import TileContent

class CellGrid:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(width)] for x in range(height)]

    def getCell(self, x:int, y:int) -> Cell:
        if x >= 0 and x < self.height and y >= 0 and y < self.width:
            return self.grid[x][y]
        else:
            raise OutOfBoundsException("CellGrid::getCell() - Cell coordinates out of bounds")
        
    def collapseCell(self, x:int, y:int, tc:TileContent) -> None:
        self.grid[x][y].collapse_to_value(tc)

    def runAlgorithm(self) -> None:
        pass

    