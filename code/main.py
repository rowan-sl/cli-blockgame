#!/usr/bin/python3.10
import tty
import sys
import queue
import threading
from time import sleep

from utils.filepath import main_path

sys.path.append(main_path)

from assets.blocks.blocks import *

from assets.templates.base.block import BaseBlock
from assets.colors import fmt, FRESET

from world import World
from player import Player

from utils.bar import get_bar
from utils.save_world import save_world
from utils.counters import Counter, RolloverCounter
from utils.clear_scr import clear_screen
from utils.sliding_window import get_window_into_area


def repr_block(value: BaseBlock):
    return f"{fmt.bgrgb(*value.background)}{fmt.fgrgb(*value.foreground)}{value.one_char_representation()}{FRESET}"


def new_display(
    area: World,
    tick_state: 1 | 2 | 3 | 4,
    health: Counter,
    oxy: Counter,
    phys_active,
    phys_tick_state: 1 | 2 | 3 | 4,
):
    tick_states = {1: "🮪", 2: "🮫", 3: "🮭", 4: "🮬"}
    ui = ""
    selection = get_window_into_area(
        area.world,
        area.player.y - 10,
        area.player.x - 10,
        area.player.y + 10,
        area.player.x + 10,
    )
    # preconvert selection into chars and rgb data
    converted_selection = []
    for row in selection:
        cvrt_row1 = []
        cvrt_row2 = []
        for block in row:
            block: BaseBlock
            chars_dat = block.char_representation()
            cvrt_row1.append(chars_dat[0])
            cvrt_row1.append(chars_dat[1])
            cvrt_row1.append(chars_dat[2])
            cvrt_row1.append(chars_dat[3])
            cvrt_row2.append(chars_dat[4])
            cvrt_row2.append(chars_dat[5])
            cvrt_row2.append(chars_dat[6])
            cvrt_row2.append(chars_dat[7])
        converted_selection.append(cvrt_row1)
        converted_selection.append(cvrt_row2)
    # actualy convert char data into the ui text
    for y, line in enumerate(converted_selection):
        for x, value in enumerate(line):
            ui += f"{fmt.bgrgb(*value[1])}{fmt.fgrgb(*value[0])}{value[2]}{FRESET}"
        ui += "\n"
    # old ui
    # tick display
    ui += f"TK{tick_states[tick_state]}  "
    # physics tick display
    ui += f"PHYSTK{tick_states[phys_tick_state]}  "
    # health
    ui += f"{fmt.FGRED}🮭🮬{FRESET} "
    ui += (
        f"{fmt.fgrgb(189,29,11)}{fmt.bgrgb(94,14,5)}{get_bar(health.value())}{FRESET}  "
    )
    # oxygen bar
    ui += f"{fmt.FGCYAN}O2{FRESET} "
    ui += (
        f"{fmt.fgrgb(179,242,255)}{fmt.bgrgb(0,51,102)}{get_bar(oxy.value())}{FRESET}  "
    )
    # debug stuff
    ui += f"PHYS:{['on' if phys_active else 'off'][0]} "
    ui += f"NOCL:{['on' if area.noclip else 'off'][0]} "
    # item UI
    ui += "\n"
    ui += f"╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗\n"
    ui += f"║🯱  ║🯲  ║🯳  ║🯴  ║🯵  ║🯶  ║🯷  ║🯸  ║🯹  ║\n"
    ui += f"║{repr_block(Stone)} ║{repr_block(Dirt)} ║{repr_block(Sand)} ║{repr_block(Grass)} ║{repr_block(Flower)} ║{repr_block(OakLog)} ║{repr_block(Leaf)} ║{repr_block(Water)} ║   ║\n"
    ui += f"╚═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╝\n".replace("╦", "╩")

    print(ui)


def input_getter(input_queue: queue.Queue):
    while True:
        txtin = sys.stdin.read(1)
        try:
            input_queue.put_nowait(txtin)
        except queue.Full:
            pass


in_queue = queue.Queue(maxsize=1)
input_reader_thread = threading.Thread(
    target=input_getter, args=[in_queue], daemon=True
)
input_reader_thread.start()

# world config
from worlds.custom import init_world

# end world config

wrld = World(init_world)

tick_st = RolloverCounter(4, 1, 1)
phys_tk_st = RolloverCounter(4, 1, 1)

health = Counter(20, 0, 20)
oxygen = Counter(20, 0, 20)

do_phys = False

# new_display(wrld, tick_st.value(), health, oxygen, do_phys, phys_tk_st.value())
# exit(1)

tty.setcbreak(sys.stdin.fileno())

clear = False
while True:
    # tps
    sleep(1 / 10)
    if tick_st.increment() == "rollover":
        clear = True
        if do_phys:
            phys_tk_st.increment()
            wrld.do_pysics()
    # handle input
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
            health.decrement()
        case "o":
            health.increment()
        case "k":
            oxygen.decrement()
        case "l":
            oxygen.increment()
        case "p":
            do_phys = not do_phys
        case _:
            pass
    if clear:
        clear_screen()
        clear = False
    new_display(wrld, tick_st.value(), health, oxygen, do_phys, phys_tk_st.value())
