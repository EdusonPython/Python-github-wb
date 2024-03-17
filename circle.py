import math
r = int(input("Ввведите радиус окружности R = "))

def area(r):
    return math.pi * r * r
S = area(r)
print("Площадь окружности S = ", S)

def perimeter(r):
    return 2 * math.pi * r
P = perimeter(r)
print("Длина окружности P = ", P)