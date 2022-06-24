# Посчитайте количество согласных букв в данной строке.

text = input("Put your text here:")
sgl = "бвгджзйклмнпрстфхцчшщ"
count = 0

for i in text:
    if i in sgl:
        count += 1
print(count)
