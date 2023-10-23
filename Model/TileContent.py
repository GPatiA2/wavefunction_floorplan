from enum import Enum, IntEnum

class TileContent(IntEnum):
    EMPTY            = 0
    
    UPPER_WALL       = 1
    LEFT_WALL        = 2
    RIGHT_WALL       = 3
    BOTTOM_WALL      = 4

    TOP_RIGHT_CORNER = 5
    TOP_LEFT_CORNER  = 6
    BOT_LEFT_CORNER  = 7
    BOT_RIGHT_CORNER = 8

    #DOOR             = 9
    BARRIER          = 9


class Side(IntEnum):

    TOP   = 0
    RIGHT = 1
    BOT   = 2
    LEFT  = 3

def get_side(srccoords, dstcoords) -> Side:

    xdiff = dstcoords[0] - srccoords[0]
    ydiff = dstcoords[1] - srccoords[1]

    if xdiff > 0  and ydiff == 0:
        return Side(1)
    elif xdiff > 0 and ydiff == 0:
        return Side(3)
    elif xdiff == 0 and ydiff > 0:
        return Side(2)
    elif xdiff == 0 and ydiff < 0:
        return Side(0)