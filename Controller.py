from TileContent import TileContent

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def onCollapse(self, x:int, y:int, tc:TileContent) -> None:
        self.view.set_content(x,y,tc)

    def collapseCell(self, x:int, y:int, tc:TileContent) -> None:
        self.model.collapseCell(x,y,tc)

    def runAlgorithm(self) -> None:
        self.model.runAlgorithm()