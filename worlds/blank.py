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
        [Air]*40
    ]*40
    player_xy = [0, 0]
    return [world, player_xy]