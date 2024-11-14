MAX_VOLUME = 8
start_points = 15

items = {
    'r': {'survival_points': 25, 'volume': 3},
    'p': {'survival_points': 15, 'volume': 2},
    'a': {'survival_points': 15, 'volume': 2},
    'm': {'survival_points': 20, 'volume': 2},
    'i': {'survival_points': 5, 'volume': 1},
    'k': {'survival_points': 15, 'volume': 1},
    'x': {'survival_points': 20, 'volume': 3},
    't': {'survival_points': 25, 'volume': 1},
    'f': {'survival_points': 15, 'volume': 1},
    'd': {'survival_points': 10, 'volume': 1},
    's': {'survival_points': 20, 'volume': 2},
    'c': {'survival_points': 20, 'volume': 2},
}

def gen_table(items, max_volume=MAX_VOLUME):
    table = [[0 for c in range(max_volume)] for _ in range(len(items))]
    for i, (_, value) in enumerate(items.items()):
        survival_points = value['survival_points']
        volume = value['volume']

        for limit_volume in range(1, max_volume + 1):
            col = limit_volume - 1
            if i == 0:
                table[i][col] = 0 if volume > limit_volume else survival_points
            else:
                prev_survival_points = table[i-1][col]
                if volume > limit_volume:
                    table[i][col] = prev_survival_points
                else:
                    used = 0 if col < volume else table[i-1][col-volume]
                    new_survival_points = used + survival_points

                    res = max(new_survival_points, prev_survival_points)
                    table[i][col] = res

    return table


if __name__ == '__main__':
    #print(*gen_table(items), sep='\n')

    #m+k+t+f+d+s - этот набор предметов максимизирует очки выживания
    #проверим, что если из этого числа очков вычесть очки за предметы,
    #которые не были взяты, то получится положительное число

    ans = []
    res_objects = ['m', 'k', 't', 'f', 'd', 's']
    sum_ost_obj = 0 #сумма оставшихся предметов

    for obj, val in items.items():
        if obj in res_objects:
            el = list(obj)
            count = val['volume']
            for _ in range(count):
                ans.append(el)
        else:
            sum_ost_obj += val['survival_points']
    points = 105 + start_points - sum_ost_obj

    for i in range(len(ans)//2):
        print(ans[i], end=' ')
    print()
    for i in range(len(ans)//2, len(ans)):
        print(ans[i], end=' ')
    print()
    print(f'Итоговые очки выживания: {points}')


