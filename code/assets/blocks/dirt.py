from assets.colors import fmt
from assets.templates.immovable_block import ImmovableBlock

class Dirt(ImmovableBlock):
    foreground = (80,59,28)
    background = (92,46,0)
    @staticmethod
    def char_representation():
        return [
            ((80,59,28), (92,46,0), "▓"),((80,59,28), (92,46,0), "▓"),
            ((80,59,28), (92,46,0), "▓"),((80,59,28), (92,46,0), "▓"),
        ]
        #return "▓"*2