from typing import List, TypeVar

from assets.blocks.blocks import WorldBorder, Void

T = TypeVar("T")


def border_world(area: List[List[T]], radius: int) -> List[List[T]]:
    new_area = []

    border = [WorldBorder]
    void = [Void]

    for _ in range(radius):
        new_area.append(void * (len(area[0]) + 2 + (radius * 2)))

    new_area.append(void*radius + border * (len(area[0]) + 2) + void*radius)

    for y, line in enumerate(area):
        # print("e")
        new_area.append((void*radius + border + line + border + void*radius))

    new_area.append(void*radius + border * (len(area[0]) + 2) + void*radius)

    for _ in range(radius):
        new_area.append(void * (len(area[0]) + 2 + (radius * 2)))

    return new_area
