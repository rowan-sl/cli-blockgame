from typing import (
    Tuple
)

class BaseBlock:
    "base of the block hierarchy, all blocks should subclass this"
    uncrossable = False
    foreground: Tuple[int, int, int]
    background: Tuple[int, int, int]
    gravity_affects: bool
    replaceable: bool = False
    self_replaceable: bool = False
    is_block: bool = True
    
    @staticmethod
    def char_representation():
        "returns a list of (forground, background, char) pairs that is 6 pairs long, 4 top 4 bottom"
        pass
    
    @staticmethod
    def one_char_representation():
        "represents the block, in a string of 2 chars (not one)"
        pass