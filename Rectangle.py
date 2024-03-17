a = int(input("Ввведите длину стороны прямоугольника a = ")) 
b = int(input("Ввведите длину стороны прямоугольника b = "))
def area(a, b):
    return a * b
S = area(a, b)
print("Площадь прямоугольника S = ", S)

def perimeter(a, b):
    return 2 * a + 2 * b
P = perimeter(a, b)
print("Периметр прямоугольника P = ", P)