def draw_line(space1, space2):
    print(f'\x1b[48;5;255m{"   " * space1}\x1b[40m{"   "}\x1b[48;5;255m{"   " * space2}\x1b[40m{"   "}\x1b[48;5;255m{"   " * space1}\x1b[0m')

def romb():
    lenn = 9
    space1 = lenn // 2
    space2 = 0
    step = 1
    center = lenn // 2 + 1
    while True:
        print(f'\x1b[48;5;255m{"   " * space1}\x1b[40m{"   "}\x1b[48;5;255m{"   " * space1}\x1b[0m')
        space2 = 1
        space1 -= 1
        for x in range(1, lenn-1):
            draw_line(space1, space2)
            if x + 1 < center:
                space1 -= step
                space2 += step * 2
            else:
                space1 += step
                space2 -= step * 2

        print(f'\x1b[48;5;255m{"   " * space1}\x1b[40m{"   "}\x1b[48;5;255m{"   " * space1}\x1b[0m')
        print('\x1b[2A')



if __name__ == "__main__":
    romb()

