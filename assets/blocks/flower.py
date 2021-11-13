from assets.colors import fmt
from assets.templates.base.block import BaseBlock
import random

class Flower(BaseBlock):
    foreground = (25,77,0)
    background = (244,255,244)
    @staticmethod
    def char_representation():
        return " ❀"
    gravity_affects = False
    replaceable = True