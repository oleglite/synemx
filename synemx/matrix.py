# -*- coding: utf-8 -*-

from synemx.defs import libmx


class Matrix:
    def __init__(self, h, w, initial_value=0.0):
        self.h = h
        self.w = w

        self.m = libmx.make_matrix(h, w, initial_value)

    def set(self, y, x, value):
        self._check_index(y, x)
        libmx.set(self.m, y, x, value)

    def get(self, y, x):
        self._check_index(y, x)
        return libmx.get(self.m, y, x)

    def _check_index(self, y, x):
        if y >= self.h or x >= self.w:
            raise IndexError('Wrong index (%s, %s) for Matrix(%s, %s)' % (y, x, self.h, self.w))
