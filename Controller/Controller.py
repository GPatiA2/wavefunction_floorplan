from Model.TileContent import TileContent
from Model.CellGrid import CellGrid
from Model.GridObserver import GridObserver

class Controller:

    def __init__(self, model : CellGrid, contentToImg):
        self.model = model
        self.contentToImg = contentToImg

    def collapseCell(self, x:int, y:int, tc:TileContent) -> None:
        self.model.collapseCell(x,y,tc)

    def addObserver(self, observer: GridObserver) -> None:
        self.model.addObserver(observer)

    def runAlgorithm(self) -> None:
        self.model.runAlgorithm()