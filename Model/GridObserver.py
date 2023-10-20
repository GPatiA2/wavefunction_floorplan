from TileContent import TileContent
from Controller.Controller import Controller

class GridObserver:

    def __init__(self, controller : Controller):
        self.controller = controller

    def onCollapse(self, x:int, y:int, tc:TileContent) -> None:
        self.controller.onCollapse(x, y, tc)