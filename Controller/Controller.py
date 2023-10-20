from Model.TileContent import TileContent
from Model.CellGrid import CellGrid
from Model.GridObserver import GridObserver
from View.MainWindow import MainWindow

class Controller:

    def __init__(self, model : CellGrid, view : MainWindow, contentToImg):
        self.model = model
        self.view = view
        self.contentToImg = contentToImg

    def onCollapse(self, x:int, y:int, tc:TileContent) -> None:
        impath = self.contentToImg[tc]
        self.view.set_content(x,y,impath)

    def collapseCell(self, x:int, y:int, tc:TileContent) -> None:
        self.model.collapseCell(x,y,tc)

    def addObserver(self, x:int, y:int, observer: GridObserver) -> None:
        self.model.addObserver(x,y,observer)

    def runAlgorithm(self) -> None:
        self.model.runAlgorithm()