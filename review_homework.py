"""Импорт инструментов абстрактного класса"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный класс для нахождения площади фигур"""
    @abstractmethod
    def get_area(self):
        """Метод нахождения площади"""
        raise NotImplementedError()

    @abstractmethod
    def get_length(self):
        """Метод нахождения длины"""
        raise NotImplementedError()


class SharpeException(Exception):
    """Создали свой класс исключения"""
    def __init__(self, description):
        super().__init__(description)

class RightTriagle(Shape):
    """Находим площадь треугольника"""
    def __init__(self, side_a, side_b, side_c):
        if not isinstance(side_a, int):
            raise ValueError("side_a is not an integer value")
        if not isinstance(side_b, int):
            raise ValueError("side_b is not an integer value")
        if not isinstance(side_c, int):
            raise ValueError("side_c is not an integer value")
        if side_a + side_b > side_c or side_b + side_c > side_a or side_a + side_c > side_b:
            raise SharpeException("Triagle sides value error")

        self.a = side_a
        self.b = side_b
        self.c = side_c


    def get_area(self):
        return (self.a * self.b) / 2

    def get_length(self):
        return super().get_length()


class Circle(Shape):
    """Находим площадь круга"""
    def __init__(self, radius):
        if not isinstance(radius, int):
            raise ValueError("radius is not an integer value")
        if radius <= 0:
            raise SharpeException("radius is less or equal to zero")
        self.r = radius

    def get_length(self):
        return 2 * 3.14 * self.r

    def get_area(self):
        return super().get_area()
