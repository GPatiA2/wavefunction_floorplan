from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Controller.Controller import Controller

class Tile(QPushButton):

    def __init__(self, controller:Controller, x:int, y:int):
        super().__init__()
        self.controller = controller
        self.x = x
        self.y = y
        self.initUI()

    def setOnClickContent(self, pathIm : str) -> None:
        self.onClickContent = pathIm

    def onClick(self) -> None:
        self.controller.collapseCell(self.x, self.y, self.onClickContent)
        self.setIcon(QIcon(self.onClickContent))

    def initUI(self) -> None:
        self.setFixedSize(50,50)
        self.clicked.connect(self.onClick)

    def setContent(self, pathIm : str) -> None:
        self.setIcon(QIcon(pathIm))
        self.setIconSize(self.size())

    
