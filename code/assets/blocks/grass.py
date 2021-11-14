from assets.colors import fmt
from assets.templates.immovable_block import ImmovableBlock

class Grass(ImmovableBlock):
    foreground = (80,59,28)
    background = (46,77,5)
    @staticmethod
    def char_representation():
        return [
            ((80,59,28), (46,77,5), "▆"),((80,59,28), (46,77,5), "▆"),((80,59,28), (46,77,5), "▆"),((80,59,28), (46,77,5), "▆"),
            ((80,59,28), (92,46,0), "▓"),((80,59,28), (92,46,0), "▓"),((80,59,28), (92,46,0), "▓"),((80,59,28), (92,46,0), "▓"),
        ]
    @staticmethod
    def one_char_representation():
        return "▆"*2