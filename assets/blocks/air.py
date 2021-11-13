from assets.colors import fmt
from assets.templates.base.block import BaseBlock

class Air(BaseBlock):
    foreground = (255, 255, 255)
    background = (255, 255, 255)
    char_representation = "█"
    gravity_affects = False
    replaceable = True