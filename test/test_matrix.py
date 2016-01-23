# -*- coding: utf-8 -*-

import pytest

from synemx.matrix import Matrix


def almost_equal(v1, v2):
    return abs(v1 - v2) < 0.000001


def matrixes_almost_equal(m1, m2):
    for r1, r2 in zip(m1.get_data(), m2.get_data()):
        for v1, v2 in zip(r1, r2):
            if not almost_equal(v1, v2):
                return False
    return True


def test_new_matrix():
    data = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ]
    m = Matrix(data)
    assert m.get_data() == data

    with pytest.raises(ValueError):
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0],
        ])

    with pytest.raises(ValueError):
        Matrix([])

    with pytest.raises(ValueError):
        Matrix([
            [],
            []
        ])


def test_create_default():
    m = Matrix.create(2, 3)

    assert m.get(0, 0) == 0.0
    assert m.get(1, 2) == 0.0

    with pytest.raises(IndexError):
        m.get(2, 2)

    with pytest.raises(IndexError):
        m.get(1, 3)

    with pytest.raises(ValueError):
        Matrix.create(0, 3)

    with pytest.raises(ValueError):
        Matrix.create(2, 0)


def test_create_with_initial_value():
    m = Matrix.create(2, 3, initial_value=0.5)

    assert m.get(0, 0) == 0.5
    assert m.get(1, 2) == 0.5


def test_set():
    m = Matrix.create(2, 3)

    m.set(0, 0, 0.5)
    assert almost_equal(m.get(0, 0), 0.5)

    m.set(1, 2, 0.6)
    assert almost_equal(m.get(1, 2), 0.6)

    with pytest.raises(IndexError):
        m.set(2, 2, 1.0)

    with pytest.raises(IndexError):
        m.set(1, 3, 1.0)


def test_get_data():
    m = Matrix.create(2, 3, 1.0)

    expected_data = [
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0],
    ]
    assert m.get_data() == expected_data

    m.set(1, 1, 2.0)
    m.set(1, 2, 3.0)

    expected_data = [
        [1.0, 1.0, 1.0],
        [1.0, 2.0, 3.0],
    ]
    assert m.get_data() == expected_data


def test_rows():
    m = Matrix.create(2, 3, 1.0)

    expected_data = [
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0],
    ]
    assert list(m.rows()) == expected_data

    m.set(1, 1, 2.0)
    m.set(1, 2, 3.0)

    expected_data = [
        [1.0, 1.0, 1.0],
        [1.0, 2.0, 3.0],
    ]
    assert list(m.rows()) == expected_data


def test_average_similarity():
    m1 = Matrix([
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ])
    m2 = Matrix([
        [0.1, 0.1, 0.1],
        [0.4, 0.4, 0.4],
    ])

    # [0] sum min = 0.3, sum max = 0.6, limit = 0.3, res = 0.3 * 0.3 / 0.6 = 0.15
    # [1] sum min = 1.2, sum max = 1.5, limit = 0.6, res = 0.6 * 1.2 / 1.5 = 0.48
    # avg = 0.315

    sim = m1.average_similarity(m2)
    assert almost_equal(sim, 0.315)

    m3 = Matrix([
        [0.1, 0.2],
        [0.4, 0.5],
    ])
    with pytest.raises(ValueError):
        m1.average_similarity(m3)

    m4 = Matrix([
        [0.1, 0.1, 0.1],
        [0.4, 0.4, 0.4],
        [0.4, 0.4, 0.4],
    ])
    with pytest.raises(ValueError):
        m1.average_similarity(m4)


def test_approximate_nothing():
    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    m2 = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])

    m1.approximate(m2, 1.0)
    expected = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    assert matrixes_almost_equal(m1, expected)


def test_approximate_zero_intensity():
    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    m2 = Matrix([
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ])

    m1.approximate(m2, 0.0)
    expected = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    assert matrixes_almost_equal(m1, expected)


def test_approximate_max_intensity():
    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    m2 = Matrix([
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ])

    m1.approximate(m2, 1.0)
    expected = Matrix([
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ])
    assert matrixes_almost_equal(m1, expected)


def test_approximate_some_intensity():
    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ])
    m2 = Matrix([
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ])

    m1.approximate(m2, 0.1)
    expected = Matrix([
        [0.9, 0.0, 0.1],
        [0.9, 0.1, 0.0],
    ])
    assert matrixes_almost_equal(m1, expected)

    m1.approximate(m2, 0.1)
    expected = Matrix([
        [0.819, 0.0, 0.19],
        [0.819, 0.19, 0.0],
    ])
    assert matrixes_almost_equal(m1, expected)
