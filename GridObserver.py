from TileContent import TileContent

class GridObserver:

    def __init__(self, controller):
        self.controller = controller

    def onCollapse(self, x:int, y:int, tc:TileContent) -> None:
        self.controller.onCollapse(x, y, tc)