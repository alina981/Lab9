from csv_tools import *
DATASET_PATH = 'books.csv'


# проивзедем поиск по автору 'Людмила Петрановская'
if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        avtor = 'Людмила Петрановская'
        title = get_title(dataset)
        lst = [s.split(';') for s in dataset]
        for el in lst:
            if el[3] == avtor:
                if 2016 <= int(el[6][6:10]) <= 2018:
                    print(el[1])
