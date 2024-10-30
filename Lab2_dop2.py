# import csv
# DATASET_PATH = 'books.csv'
#
#
# def get_title(dataset):
#     dataset.seek(0)
#     title = next(dataset)
#     title = title.split(';')
#     title = [column.strip() for column in title]
#     print(title)
#     return title
#
# def get_object_alt(line, title):
#     reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
#     res = next(reader)
#     return res
#
#
# #1 доп задание
# if __name__ == '__main__':
#     with open("books-en.csv") as dataset:
#         ans1 = []
#         title = get_title(dataset)
#         for line in dataset:
#             res = get_object_alt(line, title)
#             ans1.append(res['Publisher'])
#     print(set(ans1))

#2 доп задание
#if __name__ == '__main__':
#    with open("books-en.csv") as dataset:
#        ans = []
#        title = get_title(dataset)
#        for line in dataset:
#            res = get_object_alt(line, title)
#            ans.append(res)
#    sorted_ans = sorted(ans, key=lambda t: int(t['Downloads']), reverse=True)
#    print(sorted_ans[0:20])


open_secrets = open('letter9.txt', 'r')
stroka = ''
for word in open_secrets.read().split():
    stroka += chr(int(word))
print(stroka)