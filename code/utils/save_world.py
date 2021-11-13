from world import World

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