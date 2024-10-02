def draw_line(offset, length):
    print(f'\x1b[48;5;255m{"   " * offset}\x1b[41m{"   " * length}\x1b[48;5;255m{"   " * offset}\x1b[0m')

def circle():
    lenn = 16
    offset = lenn // 2 - 1
    length = 2
    center = lenn // 4
    step = 1
    print(f'\x1b[48;5;255m{"   " * lenn}\x1b[0m')
    for x in range(lenn // 2):
        draw_line(offset, length)
        if x+1 < center:
            offset -= step
            length += step * 2
        elif x + 1 == center:
            offset = offset
            length = length
        else:
            offset += step
            length -= step * 2
    print(f'\x1b[48;5;255m{"   " * lenn}\x1b[0m')


if __name__ == '__main__':
    circle()

