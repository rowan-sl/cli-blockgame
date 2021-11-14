def pad_right(text, target_len, char):
    text_len = len(text)
    needed_len = target_len - text_len
    if needed_len > 0:
        return text + char * needed_len
    else:
        return text
