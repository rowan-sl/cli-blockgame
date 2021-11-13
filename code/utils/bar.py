from pad_right import pad_right

BAR_STATES = [i for i in " ▄█"]


def get_bar(value):
    full_chunks = int(value/2)
    last_part_i = value%2
    if last_part_i != 0:
        last_part = BAR_STATES[last_part_i]
    else:
        last_part = ""
    return pad_right(BAR_STATES[2]*full_chunks+last_part, 10, " ")