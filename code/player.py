import sys
from utils.filepath import main_path
sys.path.append(main_path)

from assets.blocks.blocks import *
from assets.templates.base.block import BaseBlock

class Player(BaseBlock):
    gravity_affects = False
    is_block = False
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.direction = 0
        self.block_at_pl = Air

    def get_as_char(self):
        if self.direction == 0:
            return ("🯅 ", self.block_at_pl.background)
        if self.direction == -1:
            return ("🯇 ", self.block_at_pl.background)
        if self.direction == 1:
            return ("🯈 ", self.block_at_pl.background)
    
    def char_representation(self):
        chrepr = self.block_at_pl.char_representation()
        new_at_6 = ((0,0,0), chrepr[6][1], "🯅")
        chrepr[6] = new_at_6
        return chrepr