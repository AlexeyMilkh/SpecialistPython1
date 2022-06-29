# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def remainder(num_items, items_on_page):
    return num_items - items_on_page * (num_items // items_on_page)


num_items = int(input("Num item: "))
items_on_page = int(input("Items on page: "))


print(remainder(num_items, items_on_page))
