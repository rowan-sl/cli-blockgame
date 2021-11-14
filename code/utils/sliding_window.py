from typing import List, TypeVar

T = TypeVar("T")


def get_window_into_area(
    area: List[List[T]], bottom: int, left: int, top: int, right: int
) -> List[List[T]]:
    new_area = []
    max_x = len(area[0]) - 1
    max_y = len(area) - 1

    width_x = right - left
    width_y = top - bottom

    if bottom < 0:
        bottom = 0
        top = width_y
    if top > max_y:
        top = max_y
        bottom = max_y - width_y
    if left < 0:
        left = 0
        right = width_x
    if right > max_x:
        right = max_x
        left = max_x - width_x

    assert bottom >= 0
    assert left >= 0
    assert top <= max_y
    assert right <= max_x

    for y, line in enumerate(reversed(area)):
        if y <= top:
            if y >= bottom:
                new_area.append(line[left : right + 1])

    return list(reversed(new_area))
