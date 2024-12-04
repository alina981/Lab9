# Вариант 7. Все слова, начинающиеся с буквы "с"; все слова, перед которыми стоит "и" или "the"
import re


FILE = "task1-ru.txt"
FILE2 = "task1-en.txt"


with (open(FILE, encoding='utf-8') as file):
    ans1 = set()
    ans2 = set()
    for line in file:
        match1 = re.findall(r"\bс[a-zA-Zа-яА-ЯёЁ]+", line)
        match2 = re.findall(r"и\s[a-zA-Zа-яА-ЯёЁ]+", line)
        [ans1.add(el1) for el1 in match1]
        [ans2.add(el2) for el2 in match2]

print(f'Список из слов, начинающихся на букву "с", прямо перед вами :) {ans1}')
print(f'А теперь слова, перед которыми стоит "и": {ans2}')

with (open(FILE2, encoding='utf-8') as file):
    ans3 = set()
    for line in file:
        match3 = re.findall(r"the\s[a-zA-Zа-яА-ЯёЁ]+", line)
        [ans3.add(el3) for el3 in match3]

print(f'Слова, перед которыми стоит "the": {ans3}')



