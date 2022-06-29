# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

import math

def pagination(num_items, items_on_page):
    return math.ceil(num_items/items_on_page)

num_item = int(input("Num item: "))
items_on_page = int(input("Items on page: "))

print(pagination(num_item, items_on_page))

