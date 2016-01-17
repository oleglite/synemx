# -*- coding: utf-8 -*-

import pytest

from synemx.matrix import Matrix


def almost_equal(v1, v2):
    return abs(v1 - v2) < 0.000001


def test_create_default():
    m = Matrix(2, 3)

    assert m.get(0, 0) == 0.0
    assert m.get(1, 2) == 0.0

    with pytest.raises(IndexError):
        m.get(2, 2)

    with pytest.raises(IndexError):
        m.get(1, 3)


def test_create_with_initial_value():
    m = Matrix(2, 3, initial_value=0.5)

    assert m.get(0, 0) == 0.5
    assert m.get(1, 2) == 0.5


def test_set():
    m = Matrix(2, 3)

    m.set(0, 0, 0.5)
    assert almost_equal(m.get(0, 0), 0.5)

    m.set(1, 2, 0.6)
    assert almost_equal(m.get(1, 2), 0.6)

    with pytest.raises(IndexError):
        m.set(2, 2, 1.0)

    with pytest.raises(IndexError):
        m.set(1, 3, 1.0)
