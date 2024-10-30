import xml.etree.ElementTree as ET
DATASET_PATH = 'books.csv'


tree = ET.parse('currency.xml')
root = tree.getroot()
ans_index = []
k = -1
for child in root:
    for el in child:
        k += 1
        if el.tag == 'Nominal':
            if int(el.text) == 10 or int(el.text) == 100:
                ans_index.append(k-1)
k = -1
ans = []
for child in root:
    for el in child:
        k += 1
        if el.tag == 'CharCode' and k in ans_index:
            ans.append(el.text)
print(ans)