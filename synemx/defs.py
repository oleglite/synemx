# -*- coding: utf-8 -*-

from ctypes import cdll, Structure, c_uint, c_void_p, c_float, POINTER

LIBRARY_PATH = "target/release/libmx.dylib"

libmx = cdll.LoadLibrary(LIBRARY_PATH)


class Matrix(Structure):
    _fields_ = [
        ("h", c_uint),
        ("w", c_uint),
        ("matrix", c_void_p),
    ]

MatrixPointer = POINTER(Matrix)

libmx.make_matrix.argtypes = [c_uint, c_uint, c_float]
libmx.make_matrix.restype = MatrixPointer

libmx.get.argtypes = [MatrixPointer, c_uint, c_uint]
libmx.get.restype = c_float

libmx.set.argtypes = [MatrixPointer, c_uint, c_uint, c_float]
