import tty
import sys
from time import sleep
from utils.filepath import main_path
from picharsso.utils import clear_screen
sys.path.append(main_path)

from assets.blocks.blocks import (
    Sand,
    Dirt,
    Air,
    Stone,
    Grass,
    Flower,
    Leaf,
    OakLog,
    Water,
)

NOTHING_BLOCK = Air

from assets.templates.base.block import BaseBlock
from assets.colors import fmt

FRESET = fmt.MRESET

class Player:
    is_block = False
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.direction = 0
        self.block_at_pl = Air
    
    def get_as_char(self):
        if self.direction == 0:
            return ("🯅 ", self.block_at_pl.background)
        if self.direction == -1:
            return ("🯇 ", self.block_at_pl.background)
        if self.direction == 1:
            return ("🯈 ", self.block_at_pl.background)

class World:
    def __init__(self) -> None:
        # self.player = Player(0, 1)
        # from worlds.starter import init_world
        # self.world = init_world(self.player)[0]
        from worlds.custom import init_world
        self.player = Player(*init_world(None)[1])
        self.world = init_world(self.player)[0]

        self.min_x = 0
        self.min_y = 0
        self.max_x = len(self.world[0])-1
        self.max_y = len(self.world)-1

    def move_player(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy
        if new_x > self.max_x:
            print("cant move farther")
            return
        if new_x < self.min_x:
            print("cant move farther")
            return
        if new_y > self.max_y:
            print("cant move farther")
            return
        if new_y < self.min_y:
            print("cant move farther")
            return
        if self.get_from_world(self.player.x + dx, self.player.y + dy).replaceable or noclip:
            print("moving")
            #replace current loacation with prv block that was there
            self.set_in_world(self.player.x, self.player.y, self.player.block_at_pl)
            #update player vars
            self.player.x = new_x
            self.player.y = new_y
            self.player.block_at_pl = self.get_from_world(self.player.x, self.player.y)
            if dx == 0:
                self.player.direction = 0
            if dx < 0:
                self.player.direction = -1
            if dx > 0:
                self.player.direction = 1
            #set player to new location
            self.set_in_world(self.player.x, self.player.y, self.player)
        else:
            print("non-replaceable block at new location!")
    
    def place_at_player(self, block:int):
        if noclip:
            new_block = None
            match block:
                case 1:
                    new_block = Stone
                case 2:
                    new_block = Dirt
                case 3:
                    new_block = Sand
                case 4:
                    new_block = Grass
                case 5:
                    new_block = Flower
                case 6:
                    new_block = OakLog
                case 7:
                    new_block = Leaf
                case 8:
                    new_block = Water
                case _:
                    return False
            self.player.block_at_pl = new_block
    
    def place_air_at_player(self):
        self.player.block_at_pl = Air
    
    def get_from_world(self, x, y) -> BaseBlock:
        wrld_copy = list(reversed(self.world.copy()))
        return wrld_copy[y][x]

    def set_in_world(self, x, y, val):
        wrld = list(reversed(self.world.copy()))
        line = wrld[y].copy()
        line[x] = val
        wrld[y] = line
        self.world = list(reversed(wrld))

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

wrld = World()

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
    