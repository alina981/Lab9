from csv_tools import *
DATASET_PATH = 'books.csv'


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        count = 0
        title = get_title(dataset)
        lst = [s.split(';') for s in dataset]
        for el in lst:
            if len(el[1]) > 30:
                count += 1
        print(count) # количество записей, у которых в поле Название строка длиннее 30 символов

