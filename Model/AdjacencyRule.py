from TileContent import TileContent
from TileContent import Side

class AdjacencyRule:

    def __init__(self, source:TileContent, dest:TileContent, side:Side):

        self.source = source
        self.dest   = dest
        self.side   = side

    def checkValid(self, source:TileContent, dest:TileContent, side:Side) -> bool:

        source_content = self.source == source
        dest_content   = self.dest   == dest
        side_match     = self.side == side

        return source_content and dest_content and side_match