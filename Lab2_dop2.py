from csv_tools import *


if __name__ == '__main__':
   with open("books-en.csv") as dataset:
       ans = []
       title = get_title(dataset)
       for line in dataset:
           res = get_object_alt(line, title)
           ans.append(res)
   sorted_ans = sorted(ans, key=lambda t: int(t['Downloads']), reverse=True)
   print(sorted_ans[0:20])
