from TileContent import TileContent

class Tile:

    def __init__(self, x: int, y: int, c : TileContent):
        self.x = x
        self.y = y
        self.content = c

    def get_content(self) -> TileContent:
        return self.content
    
