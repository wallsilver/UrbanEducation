"""
Атрибуты класса Figure: sides_count = 0

Каждый объект класса Figure должен обладать следующими атрибутами:

Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:

Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не
изменять, в противном случае - менять.

При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать
массив с единичными сторонами и в том кол-ве, которое требует фигура.
"""

import math

class  Figure:
    sides_count = 0
    def __init__(self, color, *args):
        __sides = []
        __color = []
        if len(args) == 1:
            self.__sides = [args[0]]
            if self.sides_count > 1:
                for i in range(self.sides_count - 1):
                    self.__sides.append(args[0])
        else:
            if self.__is_valid_sides(*args) == True:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(args[i])
            else:
                self.__sides = [1]
                for i in range(self.sides_count - 1):
                    self.__sides.append(1)
        self.__color = color
        self.filled = False

    def __len__(self):
        if self.sides_count == 1:
            return self.__sides[0]
        if self.sides_count == 3:
            return self.__sides[0] + self.__sides[1] + self.__sides[2]
        if self.sides_count == 12:
            return self.__sides[0] * self.sides_count

    def __is_valid_color(self, R ,G ,B):
        if R <= 255 and R >= 0:
            if G <= 255 and G >= 0:
                if B <= 255 and B >= 0:
                    return True
        return False

    def set_color(self, R ,G ,B):
        if self.__is_valid_color(R ,G ,B) == True:
            self.__color = [R ,G ,B]
        return self.__color

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in range (len(list(new_sides))):
                if not isinstance(new_sides[i], int):
                    return False
            return True
        return False

    def set_sides(self,*new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides = [*new_sides]
        return self.__sides

    def get_sides(self):
        return self.__sides
"""
Атрибуты класса Circle: sides_count = 1

Каждый объект класса Circle должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
"""
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color, *args)
        self.__radius =  super().get_sides()[0] / 2 + math.pi

    def get_square(self):
        return math.pi * self.__radius * self.__radius

""""
Атрибуты класса Triangle: sides_count = 3

Каждый объект класса Triangle должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

"""
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *args):
        super().__init__(color, *args)

    def get_square(self, a, b, c):
        p = (a+ b +c) / 2
        return p * (p - a) * (p - b) * (p - c)

"""
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.
"""
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *args):
        super().__init__(color, *args)

    def get_volume(self):
        return super().get_sides()[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Свои проверки
print(f'\nСвои проверки\n')
triangle1 = Triangle((241, 234, 65), 12)
print(triangle1.get_color())
print(triangle1.get_sides())
triangle1.set_color(30, 70, 15) # изменится
print(triangle1.get_color())
print(len(triangle1))
triangle1.set_sides(15, 12, 10) # Изменится
print(triangle1.get_sides())
print(len(triangle1))

print(len(cube1))
circle2 = Circle((200, 200, 100), 10, 10)
cube2 = Cube((222, 35, 130), 6, 5, 3, 4, 8, 9, 5, 8, 4, 6, 3, 7)
triangle2 = Triangle((241, 234, 65), 12, 7, 4)
triangle3 = Triangle((241, 234, 65), 12, 7, 4, 3)
print(cube2.get_sides())
print(circle2.get_sides())
print(len(cube2))
print(triangle2.get_sides())
print(triangle3.get_sides())