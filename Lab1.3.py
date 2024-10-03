# по клеточкам
# def func():
#     lenn = 4
#     space = 4
#     step = 1
#     space -= step
#     for x in range(4):
#         for i in range(3):
#             print(f'{" " * space}\x1b[48;5;200m{" "}\x1b[0m')
#         space -= step
#
# if __name__ == "__main__":
#     func()


# красивее
def func():
    lenn = 12
    space = lenn - 1
    step = 1
    for i in range(lenn):
        print(f'{" " * space}\x1b[48;5;200m{" "}\x1b[0m')
        space -= step

if __name__ == "__main__":
    func()