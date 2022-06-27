# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
names = str(names)
marks = "[]'"
for x in names:
    if x in marks:
        names = names.replace(x, "")
print(names)
