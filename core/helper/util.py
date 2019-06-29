def rgb_to_hex(rgb):
    return '#%s' % ''.join(('%02x' % p for p in rgb))