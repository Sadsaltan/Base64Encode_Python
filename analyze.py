from collections import Counter
from math import log2
from os.path import getsize

filename = input("Дайте будь-ласка назву файлу (без txt) ") + ".txt"
filesize = getsize(filename)
file = open(filename, "r", encoding="utf-8")
text = file.read()
file.close()
count = Counter(text)
enthrop = 0
for k in count.keys():
    prob = count[k] / len(text)
    enthrop += prob * log2(prob)
enthrop *= -1
quantity = enthrop * len(text) / 8
print("Середня ентропія алфавіту (біт):", round(enthrop, 2))
print("Кількість інформації (байт):", round(quantity, 2))
print("Розмір файлу (байт):", filesize)
print("Різниця (байт):", round(filesize - quantity, 2))
show = input("Вивести ймовірності кожного символу? (y/other) ")
if show == 'y':
    for k in count.keys():
        if not k.isspace():
            print(f"{k}: {count[k] / len(text)}")
        else:
            print(f"U+{format(ord(k), 'x')}: {count[k] / len(text)}")
