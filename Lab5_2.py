import re


with (open("task2.txt", encoding='utf-8') as file):
    ans = []
    for line in file:
        match = re.findall(r"font-family: [a-zA-Z ']+", line)
        [ans.append(el) for el in match]
    ans_set = set()
    for x in ans:
        x = x[13:]
        ans_set.add(x)
    print(*ans_set)
