import sys
from utils.filepath import main_path
sys.path.append(main_path)

from assets.blocks.blocks import *

class Player:
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