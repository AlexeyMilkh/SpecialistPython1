# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here

def circle_in(x1, y1):
    if (r2 - r1)**2 > (x2 - x1)**2 + (y2 - y1)**2:
        return "Входит"
    else:
        return "Не входит"


x1 = int(input("X1:"))
y1 = int(input("Y1:"))
x2 = int(input("X2:"))
y2 = int(input("Y2:"))
r1 = int(input("R1"))
r2 = int(input("R2:"))

print(circle_in(x1, y1))
