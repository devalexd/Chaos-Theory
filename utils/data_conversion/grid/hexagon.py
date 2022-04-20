import math

sqrt3 = math.sqrt(3)

r'''
A             B
    \     /
       0
       |
       |
       C
'''
def convert_indices_to_coordinates(xi: int, yi: int) -> tuple[float, float]:
    return xi * sqrt3 / 2, 1.5 * yi + (1 - yi % 2) * 0.5 if xi % 2 else 1.5 * yi + yi % 2 * 0.5
def convert_coordinates_to_indices(x: float, y: float) -> tuple[int, int]:
    return round(x / sqrt3 * 2), round(y / 1.5)

dirs = [[[1, 0], [-1, 0], [0, -1]], [[1, 0], [-1, 0], [0, 1]]]


def test_convert_indices_to_coordinates():
    assert convert_indices_to_coordinates(0, 0) == (0, 0)
    assert convert_indices_to_coordinates(0, 1) == (0, 2)
    assert convert_indices_to_coordinates(0, 2) == (0, 3)
    assert convert_indices_to_coordinates(0, -1) == (0, -1)
    assert convert_indices_to_coordinates(0, -2) == (0, -3)
    assert convert_indices_to_coordinates(1, 0) == (sqrt3 / 2, 0.5)
    assert convert_indices_to_coordinates(2, 0) == (sqrt3, 0)
    assert convert_indices_to_coordinates(-1, 0) == (-sqrt3 / 2, 0.5)
    assert convert_indices_to_coordinates(-2, 0) == (-sqrt3, 0)
    assert convert_indices_to_coordinates(1, 1) == (sqrt3 / 2, 1.5)
    assert convert_indices_to_coordinates(1, 2) == (sqrt3 / 2, 3.5)
    assert convert_indices_to_coordinates(1, 3) == (sqrt3 / 2, 4.5)
    assert convert_indices_to_coordinates(3, 3) == (sqrt3 * 1.5, 4.5)
    assert convert_indices_to_coordinates(3, -3) == (sqrt3 * 1.5, -4.5)
    assert convert_indices_to_coordinates(-3, 3) == (-sqrt3 * 1.5, 4.5)
    assert convert_indices_to_coordinates(-3, -3) == (-sqrt3 * 1.5, -4.5)

def test_convert_coordinates_to_indices():
    assert convert_coordinates_to_indices(0, 0) == (0, 0)
    assert convert_coordinates_to_indices(0, 2) == (0, 1)
    assert convert_coordinates_to_indices(0, 3) == (0, 2)
    assert convert_coordinates_to_indices(0, -1) == (0, -1)
    assert convert_coordinates_to_indices(0, -3) == (0, -2)
    assert convert_coordinates_to_indices(sqrt3 / 2, 0.5) == (1, 0)
    assert convert_coordinates_to_indices(sqrt3, 0) == (2, 0)
    assert convert_coordinates_to_indices(-sqrt3 / 2, 0.5) == (-1, 0)
    assert convert_coordinates_to_indices(-sqrt3, 0) == (-2, 0)
    assert convert_coordinates_to_indices(sqrt3 / 2, 1.5) == (1, 1)
    assert convert_coordinates_to_indices(sqrt3 / 2, 3.5) == (1, 2)
    assert convert_coordinates_to_indices(sqrt3 / 2, 4.5) == (1, 3)
    assert convert_coordinates_to_indices(sqrt3 * 1.5, 4.5) == (3, 3)
    assert convert_coordinates_to_indices(sqrt3 * 1.5, -4.5) == (3, -3)
    assert convert_coordinates_to_indices(-sqrt3 * 1.5, 4.5) == (-3, 3)
    assert convert_coordinates_to_indices(-sqrt3 * 1.5, -4.5) == (-3, -3)