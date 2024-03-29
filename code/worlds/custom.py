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
    OakLog,
    Water,
)

from utils.border_world import border_world

def init_world(player):
    world = [
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Leaf,Leaf,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Leaf,OakLog,Leaf,Leaf,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Leaf,Leaf,Leaf,OakLog,OakLog,Leaf,Leaf,Leaf,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,OakLog,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,OakLog,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,OakLog,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Flower,Air,Air,Air,Air,Grass,Grass,Grass,Grass,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Dirt,Dirt,Dirt,Dirt,Grass,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Grass,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Grass,Air,Flower,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Dirt,Grass,Grass,Air,Air,player,Air,Flower,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,Air,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Dirt,Dirt,Dirt,Grass,Grass,Grass,Grass,Grass,Grass,Air,Air,Air,Air,Water,Water,Air,Air,Air,Water,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Dirt,Dirt,Dirt,Dirt,Dirt,Grass,Air,Air,Air,Air,Water,Water,Air,Air,Air,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Dirt,Dirt,Dirt,Sand,Sand,Water,Water,Water,Water,Water,Water,Water,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Sand,Water,Water,Water,Water,Water,Water,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Sand,Water,Water,Water,Water,Water,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Sand,Sand,Water,Water,Water,Water,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Sand,Sand,Sand,Sand,Sand,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,],
    [Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,Stone,],
    ]
    border_radius = 9
    world = border_world(world, border_radius)
    player_xy = [26+border_radius+1, 10+border_radius+1]
    return [world, player_xy]