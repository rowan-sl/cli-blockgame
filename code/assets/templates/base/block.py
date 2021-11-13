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
    def char_representation() -> str:
        pass