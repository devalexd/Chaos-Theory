import math

sqrt3 = math.sqrt(3)

r'''
B
  \
   A --- C
     \ /
      O
'''
def convert_indices_to_coordinates(xi: int, yi: int) -> tuple[float, float]:
    return xi - yi / 2, yi * sqrt3 / 2
def convert_coordinates_to_indices(x: float, y: float) -> tuple[int, int]:
    yi = round(y * 2 / sqrt3)
    return round(x + yi / 2), yi

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1]]


def test_convert_indices_to_coordinates():
    assert convert_indices_to_coordinates(0, 0) == (0, 0)
    assert convert_indices_to_coordinates(0, 1) == (-0.5, sqrt3 / 2)
    assert convert_indices_to_coordinates(0, 2) == (-1, sqrt3)
    assert convert_indices_to_coordinates(0, -1) == (0.5, -sqrt3 / 2)
    assert convert_indices_to_coordinates(0, -2) == (1, -sqrt3)
    assert convert_indices_to_coordinates(1, 0) == (1, 0)
    assert convert_indices_to_coordinates(2, 0) == (2, 0)
    assert convert_indices_to_coordinates(-1, 0) == (-1, 0)
    assert convert_indices_to_coordinates(-2, 0) == (-2, 0)
    assert convert_indices_to_coordinates(1, 1) == (0.5, sqrt3 / 2)
    assert convert_indices_to_coordinates(1, 2) == (0, sqrt3)
    assert convert_indices_to_coordinates(1, 3) == (-0.5, sqrt3 * 1.5)
    assert convert_indices_to_coordinates(3, 3) == (1.5, sqrt3 * 1.5)
    assert convert_indices_to_coordinates(3, -3) == (4.5, -sqrt3 * 1.5)
    assert convert_indices_to_coordinates(-3, 3) == (-4.5, sqrt3 * 1.5)
    assert convert_indices_to_coordinates(-3, -3) == (-1.5, -sqrt3 * 1.5)

def test_convert_coordinates_to_indices():
    assert convert_coordinates_to_indices(0, 0) == (0, 0)
    assert convert_coordinates_to_indices(-0.5, sqrt3 / 2) == (0, 1)
    assert convert_coordinates_to_indices(-1, sqrt3) == (0, 2)
    assert convert_coordinates_to_indices(0.5, -sqrt3 / 2) == (0, -1)
    assert convert_coordinates_to_indices(1, -sqrt3) == (0, -2)
    assert convert_coordinates_to_indices(1, 0) == (1, 0)
    assert convert_coordinates_to_indices(2, 0) == (2, 0)
    assert convert_coordinates_to_indices(-1, 0) == (-1, 0)
    assert convert_coordinates_to_indices(-2, 0) == (-2, 0)
    assert convert_coordinates_to_indices(0.5, sqrt3 / 2) == (1, 1)
    assert convert_coordinates_to_indices(0, sqrt3) == (1, 2)
    assert convert_coordinates_to_indices(-0.5, sqrt3 * 1.5) == (1, 3)
    assert convert_coordinates_to_indices(1.5, sqrt3 * 1.5) == (3, 3)
    assert convert_coordinates_to_indices(4.5, -sqrt3 * 1.5) == (3, -3)
    assert convert_coordinates_to_indices(-4.5, sqrt3 * 1.5) == (-3, 3)
    assert convert_coordinates_to_indices(-1.5, -sqrt3 * 1.5) == (-3, -3)