from PyQt5.QtWidgets import *
from Controller.Controller import Controller
from View.Tile import Tile
from Model.TileContent import TileContent
from PyQt5.QtGui import QIcon
from Model.GridObserver import GridObserver

class MainWindow(QWidget, GridObserver):

    def __init__(self, controller:Controller, width:int, height:int, contentToImg):
        super().__init__()
        self.controller = controller
        self.width_c = width 
        self.height_c = height
        self.contentToImg = contentToImg
        self.initUI()

        self.onClickContent = self.contentToImg[TileContent.EMPTY]
        self.collapsingTo = TileContent.EMPTY
        for row in self.tileGrid:
            for tile in row:
                tile.setOnClickContent(self.onClickContent, self.collapsingTo)

    def initUI(self) -> None:

        self.setWindowTitle("Automatic floor planner")
    
        self.tileGrid = [[Tile(self.controller, y, x) for x in range(self.width_c)] for y in range(self.height_c)]

        gridPannel = self.generateGridPannel()
        buttonsPannel = self.generateButtonsPannel()

        layout = QHBoxLayout()
        layout.addWidget(buttonsPannel)
        layout.addWidget(gridPannel)

        self.setLayout(layout)

    def changeOnClickContent(self, tc:TileContent) -> None:
        self.onClickContent = self.contentToImg[tc]
        for row in self.tileGrid:
            for tile in row:
                tile.setOnClickContent(self.onClickContent, tc)

    def onCollapse(self, x:int, y:int, tc:TileContent) -> None:
        k = TileContent(tc)
        self.tileGrid[x][y].setIcon(QIcon(self.contentToImg[k]))

    def generateButtonsPannel(self):
        
        buttons = []
        buttonsPannel = QWidget()

        runButton = QPushButton("Run")
        runButton.clicked.connect(self.controller.runAlgorithm)
        buttons.append(runButton)

        emptyButton = QPushButton("")
        emptyButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.EMPTY))
        emptyButton.setIcon(QIcon(self.contentToImg[TileContent.EMPTY]))
        buttons.append(emptyButton)

        upperWallButton = QPushButton("")
        upperWallButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.UPPER_WALL))
        upperWallButton.setIcon(QIcon(self.contentToImg[TileContent.UPPER_WALL]))
        buttons.append(upperWallButton)

        lowerWallButton = QPushButton("")
        lowerWallButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.LOWER_WALL))
        lowerWallButton.setIcon(QIcon(self.contentToImg[TileContent.BOTTOM_WALL]))
        buttons.append(lowerWallButton)

        rightWallButton = QPushButton("")
        rightWallButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.RIGHT_WALL))
        rightWallButton.setIcon(QIcon(self.contentToImg[TileContent.RIGHT_WALL]))
        buttons.append(rightWallButton)

        leftWallButton = QPushButton("")
        leftWallButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.LEFT_WALL))
        leftWallButton.setIcon(QIcon(self.contentToImg[TileContent.LEFT_WALL]))
        buttons.append(leftWallButton)

        topRightCornerButton = QPushButton("")
        topRightCornerButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.TOP_RIGHT_CORNER))
        topRightCornerButton.setIcon(QIcon(self.contentToImg[TileContent.TOP_RIGHT_CORNER]))
        buttons.append(topRightCornerButton)

        topLeftCornerButton = QPushButton("")
        topLeftCornerButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.TOP_LEFT_CORNER))
        topLeftCornerButton.setIcon(QIcon(self.contentToImg[TileContent.TOP_LEFT_CORNER]))
        buttons.append(topLeftCornerButton)

        botRightCornerButton = QPushButton("")
        botRightCornerButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.BOT_RIGHT_CORNER))
        botRightCornerButton.setIcon(QIcon(self.contentToImg[TileContent.BOT_RIGHT_CORNER]))
        buttons.append(botRightCornerButton)

        botLeftCornerButton = QPushButton("")
        botLeftCornerButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.BOT_LEFT_CORNER))
        botLeftCornerButton.setIcon(QIcon(self.contentToImg[TileContent.BOT_LEFT_CORNER]))  
        buttons.append(botLeftCornerButton)

        # doorButton = QPushButton("")
        # doorButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.DOOR))
        # doorButton.setIcon(QIcon(self.contentToImg[TileContent.DOOR]))
        # buttons.append(doorButton)

        barrierButton = QPushButton("")
        barrierButton.clicked.connect(lambda: self.changeOnClickContent(TileContent.BARRIER))
        barrierButton.setIcon(QIcon(self.contentToImg[TileContent.BARRIER]))
        buttons.append(barrierButton)

        layout = QVBoxLayout()
        for b in buttons:
            layout.addWidget(b)

        buttonsPannel.setLayout(layout)

        return buttonsPannel

    def generateGridPannel(self):
        
        layout = QGridLayout()
        for i in range(self.height_c):
            for j in range(self.width_c):
                layout.addWidget(self.tileGrid[i][j], i, j)
        
        gridPannel = QWidget()
        gridPannel.setLayout(layout)

        return gridPannel