from TileContent import TileContent
from TileContent import Side
from Cell import Cell

class AdjacencyRule:

    def __init__(self, source:TileContent, dest:TileContent, side:Side):

        self.source = source
        self.dest   = dest
        self.side   = side

    def checkValid(self, source:Cell, dest:Cell, side:Side) -> bool:

        source_content = self.source == source.get_content()
        dest_content   = self.dest   == dest.get_content()
        side_match     = self.side == side

        return source_content and dest_content and side_match