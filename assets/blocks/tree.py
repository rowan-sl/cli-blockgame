from assets.colors import fmt
from assets.templates.base.block import BaseBlock
from assets.templates.immovable_block import ImmovableBlock
import random

class Leaf(BaseBlock):
    foreground = (12,89,0)
    background = (8,59,0)
    @staticmethod
    def char_representation():
        return "🮐🮐"
    gravity_affects = False
    replaceable = True

class OakLog(ImmovableBlock):
    foreground = (61,42,35)
    background = (102,70,58)
    @staticmethod
    def char_representation():
        return "▏▕"