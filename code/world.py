import sys
from utils.filepath import main_path
sys.path.append(main_path)

from assets.blocks.blocks import *
from assets.templates.base.block import BaseBlock
from player import Player

class World:
    def __init__(self, init_world) -> None:
        self.player = Player(*init_world(None)[1])
        self.world = init_world(self.player)[0]

        self.noclip = False
        self.min_x = 0
        self.min_y = 0
        self.max_x = len(self.world[0])-1
        self.max_y = len(self.world)-1

    def move_player(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy
        if new_x > self.max_x:
            print("cant move farther")
            return
        if new_x < self.min_x:
            print("cant move farther")
            return
        if new_y > self.max_y:
            print("cant move farther")
            return
        if new_y < self.min_y:
            print("cant move farther")
            return
        if self.get_from_world(self.player.x + dx, self.player.y + dy).replaceable or self.noclip:
            print("moving")
            #replace current loacation with prv block that was there
            self.set_in_world(self.player.x, self.player.y, self.player.block_at_pl)
            #update player vars
            self.player.x = new_x
            self.player.y = new_y
            self.player.block_at_pl = self.get_from_world(self.player.x, self.player.y)
            if dx == 0:
                self.player.direction = 0
            if dx < 0:
                self.player.direction = -1
            if dx > 0:
                self.player.direction = 1
            #set player to new location
            self.set_in_world(self.player.x, self.player.y, self.player)
        else:
            print("non-replaceable block at new location!")
    
    def do_pysics(self):
        new = [[Air]*len(self.world[0])]*len(self.world)
        for y in (range(len(new))):
            at_min = y == 0
            for x in range(len(new[0])):
                block_at_xy = self.get_from_world(x, y)
                block_below = at_min
                if not block_below:
                    if not self.get_from_world(x, y-1, new).replaceable:
                        #there is a block below us, and its not replaceable
                        block_below = True
                    else:
                        #no block below
                        block_below = False
                if block_below:
                    new = self.set_in_world(x, y, block_at_xy, new)
                else:
                    if block_at_xy.gravity_affects:
                        #block is going to be replaced
                        block_below_xy = self.get_from_world(x, y-1, new)
                        if block_below_xy.self_replaceable:
                            new = self.set_in_world(x, y-1, block_at_xy, new)
                        else:
                            if block_below_xy == block_at_xy:
                                new = self.set_in_world(x, y, block_at_xy, new)
                            else:
                                print("e")
                                new = self.set_in_world(x, y-1, block_at_xy, new)
                    else:
                        new = self.set_in_world(x, y, block_at_xy, new)
        self.world = new
    
    def place_at_player(self, block:int):
        if self.noclip:
            new_block = None
            match block:
                case 1:
                    new_block = Stone
                case 2:
                    new_block = Dirt
                case 3:
                    new_block = Sand
                case 4:
                    new_block = Grass
                case 5:
                    new_block = Flower
                case 6:
                    new_block = OakLog
                case 7:
                    new_block = Leaf
                case 8:
                    new_block = Water
                case _:
                    return False
            self.player.block_at_pl = new_block
    
    def place_air_at_player(self):
        self.player.block_at_pl = Air
    
    def get_from_world(self, x, y, world=None) -> BaseBlock:
        if world is None:
            wrld_copy = list(reversed(self.world.copy()))
            return wrld_copy[y][x]
        else:
            wrld_copy = list(reversed(world))
            return wrld_copy[y][x]

    def set_in_world(self, x, y, val, world=None):
        if world is None:
            wrld = list(reversed(self.world.copy()))
            line = wrld[y].copy()
            line[x] = val
            wrld[y] = line
            self.world = list(reversed(wrld))
        else:
            wrld = list(reversed(world))
            line = wrld[y].copy()
            line[x] = val
            wrld[y] = line
            return list(reversed(wrld))
    
    def update_noclip(self, noclip: bool) -> None:
        self.noclip = noclip