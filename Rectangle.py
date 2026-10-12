# ввод длины
length = float(input("Введите длину прямогольника: "))

# ввод ширины
width = float(input("Введите ширину прямогольника: "))


def rectangle_area(length,width):
    area = length * width
    print("Площадь равна =", area)


def rectangle_perimetr(length,width):
    perimetr = 2 * length + 2 * width
    print("Периметр равен =", perimetr)


rectangle_area(length,width)

rectangle_perimetr(length,width)
