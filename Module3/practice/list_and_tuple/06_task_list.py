# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here

a = int(input("Put number: "))
b = int(input("Put number: "))

for i in range(a,b):
    if i % 3 == 0:
        print(i, end=" ")
