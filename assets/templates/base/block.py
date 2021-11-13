from typing import (
    Tuple
)

class BaseBlock:
    "base of the block hierarchy, all blocks should subclass this"
    foreground: Tuple[int, int, int]
    background: Tuple[int, int, int]
    char_representation: str
    gravity_affects: bool
    replaceable: bool = False