import argparse
from Model.CellGrid import CellGrid
from Model.AdjacencyRule import AdjacencyRule
from Model.TileContent import TileContent, Side

from View.MainWindow import MainWindow
from Controller.Controller import Controller

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

import json

def options():

    parser = argparse.ArgumentParser(description="Automatic floor planner")
    parser.add_argument("-w", "--width", type=int, default=10, help="Width of the grid")
    parser.add_argument("-h", "--height", type=int, default=10, help="Height of the grid")
    parser.add_argument("-r", "--rules_file", type=str, help="File containing adjacency rules")
    parser.add_argument("-i", "--icons_file", type=str, help="File containing icons paths")
    opt = parser.parse_args()
    print(opt)
    return opt

def getReciprocalSide(side:Side) -> Side:

    if side == Side.TOP:
        return Side.BOT
    elif side == Side.BOT:
        return Side.TOP
    elif side == Side.LEFT:
        return Side.RIGHT
    elif side == Side.RIGHT:
        return Side.LEFT

def parseAdjacencyRules(jsonRules:dict) -> list:

    rules = []
    for rule in jsonRules:
        src = TileContent[rule["src"].upper()]
        dst = TileContent[rule["dst"].upper()]
        side = Side[rule["side"].upper()]
        rules.append(AdjacencyRule(src, dst, side))
        rules.append(AdjacencyRule(dst, src, getReciprocalSide(side)))

    return rules

def parseFileIcons(jsonIcons:dict) -> dict:

    icons = {}
    for icon in jsonIcons:
        content = TileContent[icon["content"].upper()]
        path = icon["path"]
        icons[content] = path

    return icons

def main():

    args = options()

    with open(args.rules_file, "r") as f:
        rules = json.load(f)

    with open(args.icons_file, "r") as f:
        icons = json.load(f)

    adjrules = parseAdjacencyRules(rules)
    contentToImg = parseFileIcons(icons)

    app = QApplication([])

    model = CellGrid(args.width, args.height, adjrules)
    controller = Controller(model, contentToImg)
    view = MainWindow(controller, args.width, args.height, contentToImg)
    controller.addObserver(view)

    window = QMainWindow()
    window.setCentralWidget(view)

    sys.exit(app.exec_())