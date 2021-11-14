from assets.colors import fmt
from assets.templates.moveable_block import MoveableBlock

class Sand(MoveableBlock):
    foreground = (194,178,128)
    background = (184,126,50)
    @staticmethod
    def char_representation():
        return [
            ((194,178,128),(184,126,50), "░"),
        ]*8
    @staticmethod
    def one_char_representation():
        return "░"*2