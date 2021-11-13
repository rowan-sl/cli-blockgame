from time import sleep
import sys
from utils.filepath import main_path
from utils.term_utils import clear_screen, reset_cursor
sys.path.append(main_path)
# from colors import fmt

from assets.blocks.blocks import (
    Sand,
    Dirt,
    Air,
    Stone,
    Grass,
)

NOTHING_BLOCK = Air

from assets.templates.base.block import BaseBlock
from assets.colors import fmt

FRESET = fmt.MRESET

world =[
[Sand]*2 + [Air]*6,
[Air]*8,
[Air,   Air,   Grass, Grass, Grass, Grass, Grass, Grass],
[Air,   Air,   Dirt,  Dirt,  Dirt,  Dirt,  Dirt,  Dirt ],
[Air,   Stone, Stone, Stone, Stone, Dirt,  Dirt,  Stone],
[Stone, Stone, Stone, Stone, Stone, Stone, Stone, Air  ],
]

def get_from_world(x, y, wrld) -> BaseBlock:
    wrld_copy = list(reversed(wrld.copy()))
    return wrld_copy[y][x]

def set_in_world(x, y, val, wrld):
    wrld = list(reversed(wrld.copy()))
    line = wrld[y].copy()
    line[x] = val
    wrld[y] = line
    return list(reversed(wrld))

def update(area: list):
    new = [[NOTHING_BLOCK]*len(area[0])]*len(area)
    for y in (range(len(new))):
        at_min = y == 0
        for x in range(len(new[0])):
            block_at_xy = get_from_world(x, y, area)
            block_below = at_min
            if not block_below:
                if not get_from_world(x, y-1, new).replaceable:
                    #there is a block below us, and its not replaceable
                    block_below = True
                else:
                    #no block below
                    block_below = False
            if block_below:
                new = set_in_world(x, y, block_at_xy, new)
            else:
                if block_at_xy.gravity_affects:
                    new = set_in_world(x, y-1, block_at_xy, new)
                else:
                    new = set_in_world(x, y, block_at_xy, new)
    return new

