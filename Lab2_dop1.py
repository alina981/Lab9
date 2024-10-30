from csv_tools import *


if __name__ == '__main__':
    with open("books-en.csv") as dataset:
        ans1 = []
        title = get_title(dataset)
        for line in dataset:
            res = get_object_alt(line, title)
            ans1.append(res['Publisher'])
    print(set(ans1))