import tty
import sys
from time import sleep
import threading
import queue
from utils.filepath import main_path
from picharsso.utils import clear_screen
sys.path.append(main_path)

from assets.blocks.blocks import *

from assets.templates.base.block import BaseBlock
from assets.colors import fmt

FRESET = fmt.MRESET

from world import World
from player import Player

#set this to true to clear before all the tick calcluations happen, this causes flashing, but also shows print statements that happen while tick is being executed
DEBUGCLEAR = False

BAR_STATES = [i for i in " ▄█"]

def pad_right(text, target_len, char):
    text_len = len(text)
    needed_len = target_len-text_len
    if needed_len > 0:
        return text+char*needed_len
    else:
        return text

def get_health_bar(health):
    full_chunks = int(health/2)
    last_part_i = health%2
    if last_part_i != 0:
        last_part = BAR_STATES[last_part_i]
    else:
        last_part = ""
    return pad_right(BAR_STATES[2]*full_chunks+last_part, 10, " ")

def repr_block(value):
    return  f"{fmt.bgrgb(*value.background)}{fmt.fgrgb(*value.foreground)}{value.char_representation()}{FRESET}"

def display(area: World, tick_state: 1|2|3|4, health):
    tick_states = {1: "🮪", 2: "🮫", 3: "🮭", 4: "🮬"}
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
    converted += f"{tick_states[tick_state]}  "
    converted += f"{fmt.FGRED}🮭🮬{FRESET} "
    converted += f"{fmt.fgrgb(189,29,11)}{fmt.bgrgb(94,14,5)}{get_health_bar(health)}{FRESET}"
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

def input_getter(input_queue: queue.Queue):
    while True:
        txtin = sys.stdin.read(1)
        try:
            input_queue.put_nowait(txtin)
        except queue.Full:
            pass

in_queue = queue.Queue(maxsize=3)
input_reader_thread = threading.Thread(target=input_getter, args=[in_queue], daemon=True)
input_reader_thread.start()

#world config
from worlds.custom import init_world
#end world config

wrld = World(init_world)

tick_state = 1

health = 20
max_health = 20
min_health = 0

while True:
    #tps
    sleep(1/10)
    if tick_state < 4:
        tick_state += 1
    else:
        tick_state = 1
    if DEBUGCLEAR: print("\x1b[2J")#clear_screen()
    #handle input
    text = ""
    try:
        text = in_queue.get_nowait()
    except queue.Empty:
        pass
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
            wrld.update_noclip(not wrld.noclip)
        case text if text in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            wrld.place_at_player(int(text))
        case "f":
            save_world(wrld)
        case "x":
            wrld.place_air_at_player()
        case "i":
            if health > min_health:
                health -= 1
        case "o":
            if health < max_health:
                health += 1
        case _:
            pass
    if not DEBUGCLEAR: print("\x1b[2J")#clear_screen()
    display(wrld, tick_state, health)
    