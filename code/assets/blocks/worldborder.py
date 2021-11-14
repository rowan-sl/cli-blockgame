from assets.templates.base.block import BaseBlock
from assets.blocks.air import Air

class WorldBorder(BaseBlock):
    uncrossable = True
    foreground = (77,166,255)
    background = (102,230,255)
    gravity_affects = False
    replaceable: bool = False
    self_replaceable: bool = False
    is_block: bool = True

    @staticmethod
    def char_representation():
        return [
            ((77,166,255),(102,230,255), "🮘"), ((77,166,255),(102,230,255), "🮘"), ((77,166,255),(102,230,255), "🮘"),((77,166,255),(102,230,255), "🮘"),
            ((77,166,255),(102,230,255), "🮙"), ((77,166,255),(102,230,255), "🮘"), ((77,166,255),(102,230,255), "🮘"),((77,166,255),(102,230,255), "🮘"),
        ]

    @staticmethod
    def one_char_representation() -> str:
        return "🮘"*2

class Void(Air):
    foreground = (40,40,40)
    background = (0,0,0)
    @staticmethod
    def char_representation():
        return [
            ((40,40,40), (0,0,0), "🮐"),
        ]*8
    @staticmethod
    def one_char_representation() -> str:
        return "🮐"*2