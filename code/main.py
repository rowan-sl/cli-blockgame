import tty
import sys
from time import sleep
from utils.filepath import main_path
from picharsso.utils import clear_screen
sys.path.append(main_path)

from assets.blocks.blocks import *

from assets.templates.base.block import BaseBlock
from assets.colors import fmt

FRESET = fmt.MRESET

from world import World
from player import Player

def repr_block(value):
    return  f"{fmt.bgrgb(*value.background)}{fmt.fgrgb(*value.foreground)}{value.char_representation()}{FRESET}"

def display(area: World):
    #convert 0 and 1 to block and space
    converted = ""
    for y, line in enumerate(area.world):
        for _ in range(1):
            for x, value in enumerate(line):
                if value.is_block:
                    converted += f"{fmt.bgrgb(*value.background)}{fmt.fgrgb(*value.foreground)}{value.char_representation()}{FRESET}"
                else:
                    player_repr = area.player.get_as_char()
                    converted += f"{fmt.bgrgb(*player_repr[1])}{fmt.fgrgb(0, 0, 0)}{player_repr[0]}{FRESET}"
            converted += "\n"
    converted += f"╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗\n"
    converted += f"║🯱  ║🯲  ║🯳  ║🯴  ║🯵  ║🯶  ║🯷  ║🯸  ║🯹  ║\n"
    converted += f"║{repr_block(Stone)} ║{repr_block(Dirt)} ║{repr_block(Sand)} ║{repr_block(Grass)} ║{repr_block(Flower)} ║{repr_block(OakLog)} ║{repr_block(Leaf)} ║{repr_block(Water)} ║\n"
    converted += f"╚═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╝\n".replace("╦", "╩")
    print(converted)

def save_world(world: World):
    print("world = [")
    for row in world.world:
        print("[", end="")
        for block in row:
            try:
                print(block.__name__+",", end="")
            except AttributeError:
                print("player,", end="")
        print("],")
    print("]")
    print(f"player_xy = [{world.player.x}, {world.player.y}]")

tty.setcbreak(sys.stdin.fileno())

#world config
from worlds.custom import init_world
#end world config

wrld = World(init_world)

noclip = False
while True:
    text = sys.stdin.read(1)
    clear_screen()
    match text.lower():
        case "w":
            wrld.move_player(0, 1)
        case "s":
            wrld.move_player(0, -1)
        case "a":
            wrld.move_player(-1, 0)
        case "d":
            wrld.move_player(1, 0)
        case "n":
            print("")
            noclip = not noclip
        case text if text in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("")
            wrld.place_at_player(int(text))
        case "f":
            save_world(wrld)
        case "x":
            print("")
            wrld.place_air_at_player()
        case _:
            pass
    print("noclip", noclip)
    display(wrld)
    