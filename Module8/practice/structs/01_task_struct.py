# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]

feet = []
for x in distances:
    feet.append(3.28*int(x))

print(feet)
