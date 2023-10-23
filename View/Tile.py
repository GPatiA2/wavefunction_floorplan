from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Controller.Controller import Controller
from Model.TileContent import TileContent

class Tile(QPushButton):

    def __init__(self, controller:Controller, x:int, y:int):
        super().__init__()
        self.controller = controller
        self.x_pos = x
        self.y_pos = y
        self.initUI()

    def setOnClickContent(self, pathIm : str, collapsingTo : TileContent) -> None:
        self.onClickContent = pathIm
        self.collapsingTo = collapsingTo

    def onClick(self) -> None:
        print("Clicking on cell ({}, {})".format(self.x_pos, self.y_pos))
        self.controller.collapseCell(self.x_pos, self.y_pos, self.collapsingTo)
        self.setIcon(QIcon(self.onClickContent))

    def initUI(self) -> None:
        self.setFixedSize(50,50)
        self.clicked.connect(self.onClick)

    def setContent(self, pathIm : str) -> None:
        self.setIcon(QIcon(pathIm))
        self.setIconSize(self.size())

    
