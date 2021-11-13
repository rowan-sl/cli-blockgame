import sys
from utils.filepath import main_path
sys.path.append(main_path)

from assets.blocks.blocks import (
    Sand,
    Dirt,
    Air,
    Stone,
    Grass,
    Flower,
    Leaf,
    OakLog
)

def init_world(player):
    world =[
        [Sand]*2 + [Air]*6,
        [Air]*8,
        [Air]*8,
        [Air]*8,
        [Air,   Air,       Grass, Grass, Grass, Grass, Grass, Grass],
        [Air,   Air,       Dirt,  Dirt,  Dirt,  Dirt,  Dirt,  Dirt ],
        [player,Stone,Stone, Stone, Stone, Dirt,  Dirt,  Stone],
        [Air, Stone,       Stone, Stone, Stone, Stone, Stone, Air  ],
    ]
    player_xy = [0, 1]
    return [world, player_xy]