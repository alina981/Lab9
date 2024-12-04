import re
import csv


with (open("task3.txt", encoding='utf-8') as file):
    ans = []
    for line in file:
        e_mail = re.findall(r"[a-zA-Z_0-9]+[@][a-zA-Z_-]+[.][netcombizfrg]+[motzg]", line)
        site_http = re.findall(r"http://\S+[/]", line)
        site_https = re.findall(r"https://\S+[/]", line)
        data = re.findall(r"\d\d\d\d[-]\d\d[-]\d\d", line)
        name= re.findall(r"[A-Z][a-z]+", line)
    site = []
    for el in site_http:
        site.append(el)
    for el in site_https:
        site.append(el)



with open("lab5.csv", mode="w", encoding='utf-8') as w_file:
    titles = ["Фамилия", "Электронная почта", "Дата регистрации", "Сайт"]
    file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator="\r", fieldnames=titles)
    file_writer.writeheader()
    for i in range(len(name)):
        file_writer.writerow({"Фамилия": name[i], "Электронная почта": e_mail[i], "Дата регистрации": data[i], "Сайт": site[i]})



