# coding: utf-8

import math


class Figure:
    def __init__(self, coors):
        self.coors = coors

    @staticmethod
    def _get_length(a, b):
        ab = abs(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2))
        return ab

    def get_lengths(self):
        lengths = []
        for i, coor1 in enumerate(self.coors):
            for j, coor2 in enumerate(self.coors):
                if j > i:
                    lengths.append(self._get_length(coor1, coor2))
        return lengths

    def get_perimeter(self):
        overall_sum = 0
        lengths = self.get_lengths()
        for length in lengths:
            overall_sum += length
        return round(overall_sum, 3)


class Triangle(Figure):
    def __init__(self, coors):
        Figure.__init__(self, coors)
        self.a = self.coors[0]
        self.b = self.coors[1]
        self.c = self.coors[2]

    def get_area(self):
        op1 = (self.a[0] - self.c[0]) * (self.b[1] - self.c[1])
        op2 = (self.b[0] - self.c[0]) * (self.a[1] - self.c[1])
        s = 0.5 * (op1 - op2)
        s = int(s) if s.is_integer() else abs(s)
        return s

    def get_height(self):
        bc = self._get_length(self.b, self.c)
        ac = self._get_length(self.a, self.c)
        ab = self._get_length(self.a, self.b)

        height_a = (2 * self.get_area()) / abs(bc)
        height_a = int(height_a) if height_a.is_integer() else round(height_a, 3)

        height_b = (2 * self.get_area()) / abs(ac)
        height_b = int(height_b) if height_b.is_integer() else round(height_b, 3)

        height_c = (2 * self.get_area()) / abs(ab)
        height_c = int(height_c) if height_c.is_integer() else round(height_c, 3)

        return [height_a, height_b, height_c]


class Trapeze(Figure):
    def __init__(self, coors):
        Figure.__init__(self, coors)

    def get_area(self):
        base1, base2 = 0, 0
        base1_y, base2_y = None, None
        for coor1 in self.coors:
            for coor2 in self.coors:
                if coor1 is not coor2:
                    if coor1[1] == coor2[1] and base1_y is None:
                        base1_y = coor1[1]
                        base1 = round(abs(self._get_length(coor1, coor2)), 3)
                    elif coor1[1] == coor2[1] and base1_y != coor1[1]:
                        base2_y = coor1[1]
                        base2 = round(abs(self._get_length(coor1, coor2)), 3)

        s = abs((base1 + base2) / 2 * (base1_y - base2_y))
        s = int(s) if s.is_integer else s
        return s


triangle = Triangle([[-3, -2], [-1, 1], [2, 3]])
triangle_heights = triangle.get_height()

trapeze = Trapeze([[3, 2], [5, 2], [9, 6], [6, 6]])

print('Площадь треугольника: {}'.format(triangle.get_area()))
print('Высота треугольника из вершины A: {}'.format(triangle_heights[0]))
print('Высота треугольника из вершины B: {}'.format(triangle_heights[1]))
print('Высота треугольника из вершины C: {}'.format(triangle_heights[2]))
print('Периметр треугольника: {}'.format(triangle.get_perimeter()))

print('\nПлощадь трапеции: {}'.format(trapeze.get_area()))
print('Периметр трапеции: {}'.format(trapeze.get_perimeter()))
print('Длины сторон трапеции: {}'.format(' '.join(str(x) for x in trapeze.get_lengths())))
