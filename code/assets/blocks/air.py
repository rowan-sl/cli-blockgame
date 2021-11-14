from assets.colors import fmt
from assets.templates.base.block import BaseBlock

class Air(BaseBlock):
    foreground = (255, 255, 255)
    background = (255, 255, 255)
    @staticmethod
    def char_representation():
        return [
            ((255, 255, 255), (255, 255, 255), "█"),((255, 255, 255), (255, 255, 255), "█"),
            ((255, 255, 255), (255, 255, 255), "█"),((255, 255, 255), (255, 255, 255), "█"),
        ]
        #return "█"*2
    gravity_affects = False
    replaceable = True