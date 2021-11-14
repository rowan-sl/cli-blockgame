from assets.colors import fmt
from assets.templates.immovable_block import ImmovableBlock

class Stone(ImmovableBlock):
    foreground = (59,58,56)
    background = (66,66,66)
    @staticmethod
    def char_representation():
        return [
            ((59,58,56),(66,66,66), "▒"),
        ]*8
    @staticmethod
    def one_char_representation():
        return "▒"*2