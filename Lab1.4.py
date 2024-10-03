with open('sequence.txt') as file:
    lst = [float(s) for s in file]
    numbers_b = []
    numbers_m = []
    for el in lst:
        if el <= 0:
            if el > -5:
                numbers_b.append(el)
            elif el < -5:
                numbers_m.append(el)
print(len(lst), '- всего чисел')
print(len(numbers_b),  '- >-5, 28%, 1-ая колонка')
print(len(numbers_m), '- <-5, 21%, 2-ая колонка')

#в последовательности 71 число, большее -5(28%); 53 числа, меньших -5(21%); всего чисел 250


def diagr():
    print()
    print()
    print('кол-во %')
    print(" " * 3 + f'\x1b[48;5;128m {" "}\x1b[0m')
    print(" " * 2 + f'\x1b[48;5;128m {" " * 3}\x1b[0m')
    for x in range(10):
        print(" " * 3 + f'\x1b[48;5;128m {" "}\x1b[0m')
    print("28%" + f'\x1b[48;5;128m {" "}\x1b[0m' + " " * 4 + f'\x1b[48;5;200m {" "}\x1b[0m')
    print("21%" + f'\x1b[48;5;128m {" "}\x1b[0m' + " " * 4 + f'\x1b[48;5;200m {" "}\x1b[0m' + " " * 4
          + f'\x1b[48;5;200m {" "}\x1b[0m')
    print(" " * 3 + f'\x1b[48;5;128m {" "}\x1b[0m' + " " * 4 + f'\x1b[48;5;200m {" "}\x1b[0m' + " " * 4
          + f'\x1b[48;5;200m {" "}\x1b[0m')
    print(" " * 3 + f'\x1b[48;5;128m {" "}\x1b[0m' + " " * 4 + f'\x1b[48;5;200m {" "}\x1b[0m' + " " * 4
          + f'\x1b[48;5;200m {" "}\x1b[0m' + " " * 13 + f'\x1b[48;5;128m {" "}\x1b[0m')
    print(" " * 3 + f'\x1b[48;5;128m {" " * 29}\x1b[0m' + "   группа чисел")
    print(" " * 9 + ">-5" + " " * 3 + "<-5" + " " * 12 + f'\x1b[48;5;128m {" "}\x1b[0m')


if __name__ == "__main__":
    diagr()
