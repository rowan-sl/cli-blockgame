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

from utils.bar import get_bar

def repr_block(value):
    return  f"{fmt.bgrgb(*value.background)}{fmt.fgrgb(*value.foreground)}{value.char_representation()}{FRESET}"

def display(area: World, tick_state: 1|2|3|4, health, oxy, phys_active, phys_tick_state):
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
    #tick display
    converted += f"TK{tick_states[tick_state]}  "
    #physics tick display
    converted += f"PHYSTK{tick_states[phys_tick_state]}  "
    #health
    converted += f"{fmt.FGRED}🮭🮬{FRESET} "
    converted += f"{fmt.fgrgb(189,29,11)}{fmt.bgrgb(94,14,5)}{get_bar(health)}{FRESET}  "
    #oxygen bar
    converted += f"{fmt.FGCYAN}O2{FRESET} "
    converted += f"{fmt.fgrgb(179,242,255)}{fmt.bgrgb(0,51,102)}{get_bar(oxy)}{FRESET}  "
    #debug stuff
    converted += f"PHYS:{['on' if phys_active else 'off'][0]} "
    converted += f"NOCL:{['on' if area.noclip else 'off'][0]} "
    #item UI
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
phys_tick_state = 1

health = 20
max_health = 20
min_health = 0

oxygen = 20
max_oxy = 20
min_oxy = 0

do_phys = False

while True:
    #tps
    sleep(1/10)
    if tick_state < 4:
        tick_state += 1
    else:
        tick_state = 1
        print("\x1b[2J")
        if do_phys:
            if phys_tick_state < 4:
                phys_tick_state += 1
            else:
                phys_tick_state = 1
            wrld.do_pysics()
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
            print("please press ctrl+C")
            sleep(10)
        case "x":
            wrld.place_air_at_player()
        case "i":
            if health > min_health:
                health -= 1
        case "o":
            if health < max_health:
                health += 1
        case "k":
            if oxygen > min_oxy:
                oxygen -= 1
        case "l":
            if oxygen < max_oxy:
                oxygen += 1
        case "p":
            do_phys = not do_phys
        case _:
            pass
    display(wrld, tick_state, health, oxygen, do_phys, phys_tick_state)
    