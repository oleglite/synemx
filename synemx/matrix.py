# -*- coding: utf-8 -*-

from synemx.defs import libmx, to_float_array


class Matrix:
    def __init__(self, data=None, uninitialized=False):
        if uninitialized:
            return

        if not data or not all(data):
            raise ValueError("Can't create empty Matrix")

        if not all(len(v) == len(data[0]) for v in data):
            raise ValueError('All rows must have the same size: %s' % data)

        self.h = len(data)
        self.w = len(data[0])
        values = [v for row in data for v in row]
        self.m = libmx.matrix_new(self.h, self.w, to_float_array(values))

    @classmethod
    def create(cls, h, w, initial_value=0.0):
        if h <= 0 or w <= 0:
            raise ValueError("Can't create empty Matrix")

        matrix = cls(uninitialized=True)

        matrix.h = h
        matrix.w = w
        matrix.m = libmx.matrix_create(h, w, initial_value)
        return matrix

    def get(self, y, x):
        self._check_index(y, x)
        return libmx.matrix_get(self.m, y, x)

    def set(self, y, x, value):
        self._check_index(y, x)
        libmx.matrix_set(self.m, y, x, value)

    def rows(self):
        return iter(self.get_data())

    def get_data(self):
        return [
           [libmx.matrix_get(self.m, y, x) for x in range(self.w)]
           for y in range(self.h)
        ]

    def average_similarity(self, other):
        self._check_size(other)
        return libmx.matrix_average_similarity(self.m, other.m)

    def approximate(self, other, factor):
        self._check_size(other)
        libmx.matrix_approximate(self.m, other.m, factor)

    def _check_index(self, y, x):
        if y >= self.h or x >= self.w:
            raise IndexError('Wrong index (%s, %s) for Matrix(%s, %s)' % (y, x, self.h, self.w))

    def _check_size(self, other):
        if not (self.h == other.h and self.w == other.w):
            raise ValueError('Can\'t compare matrixes with different sizes')

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.get_data() == other.get_data()

    def __repr__(self):
        result = 'Matrix([\n    %s\n])' % (',\n    '.join(map(str, self.get_data())))
        return result
