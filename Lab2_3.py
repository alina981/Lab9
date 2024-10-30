from csv_tools import *
DATASET_PATH = 'books.csv'


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        k = 1
        res = []
        title = get_title(dataset)
        lst = [s.split(';') for s in dataset]
        for el in lst:
            if k <= 20:
                line = f'{k} {el[3]}. {el[1]} - {el[6][6:10]}\n'
                k += 1
                res.append(line)
    with open("new_file", 'w') as out:
        out.writelines(res)