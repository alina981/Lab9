import csv
DATASET_PATH = 'books.csv'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [column.strip() for column in title]
    print(title)
    return title

def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res

#1 задание
if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        count = 0
        title = get_title(dataset)
        lst = [s.split(';') for s in dataset]
        for el in lst:
            if len(el[1]) > 30:
                count += 1
        print(count) # количество записей, у которых в поле Название строка длиннее 30 символов

# #2 задание, проивзедем поиск по автору 'Людмила Петрановская'
# if __name__ == '__main__':
#     with open(DATASET_PATH) as dataset:
#         avtor = 'Людмила Петрановская'
#         title = get_title(dataset)
#         lst = [s.split(';') for s in dataset]
#         for el in lst:
#             if el[3] == avtor:
#                 if 2016 <= int(el[6][6:10]) <= 2018:
#                     print(el[1])

# #3 задание
# if __name__ == '__main__':
#     with open(DATASET_PATH) as dataset:
#         k = 1
#         res = []
#         title = get_title(dataset)
#         lst = [s.split(';') for s in dataset]
#         for el in lst:
#             if k <= 20:
#                 line = f'{k} {el[3]}. {el[1]} - {el[6][6:10]}\n'
#                 k += 1
#                 res.append(line)
#     with open("new_file", 'w') as out:
#         out.writelines(res)

# #4 задание
# import xml.etree.ElementTree as ET
# tree = ET.parse('currency.xml')
# root = tree.getroot()
# ans_index = []
# k = -1
# for child in root:
#     for el in child:
#         k += 1
#         if el.tag == 'Nominal':
#             if int(el.text) == 10 or int(el.text) == 100:
#                 ans_index.append(k-1)
# k = -1
# ans = []
# for child in root:
#     for el in child:
#         k += 1
#         if el.tag == 'CharCode' and k in ans_index:
#             ans.append(el.text)
# print(ans)
