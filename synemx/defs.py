# -*- coding: utf-8 -*-

from ctypes import cdll, Structure, c_size_t, c_void_p, c_float, POINTER

LIBRARY_PATH = "target/release/libmx.dylib"

libmx = cdll.LoadLibrary(LIBRARY_PATH)


def to_float_array(l):
    return (c_float * len(l))(*l)


class Matrix(Structure):
    _fields_ = [
        ("h", c_size_t),
        ("w", c_size_t),
        ("matrix", c_void_p),
    ]

MatrixPointer = POINTER(Matrix)

libmx.matrix_new.argtypes = [c_size_t, c_size_t, POINTER(c_float)]
libmx.matrix_new.restype = MatrixPointer

libmx.matrix_create.argtypes = [c_size_t, c_size_t, c_float]
libmx.matrix_create.restype = MatrixPointer

libmx.matrix_get.argtypes = [MatrixPointer, c_size_t, c_size_t]
libmx.matrix_get.restype = c_float

libmx.matrix_set.argtypes = [MatrixPointer, c_size_t, c_size_t, c_float]
