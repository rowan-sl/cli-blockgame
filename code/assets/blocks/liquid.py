from assets.colors import fmt
from assets.templates.base.block import BaseBlock

class Water(BaseBlock):
    foreground = (84,187,255)
    background = (204,247,255)
    @staticmethod
    def char_representation():
        return "🮐"*2
    gravity_affects = True
    replaceable = True
    self_replaceable = False