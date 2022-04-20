r'''
Diffusion-limited aggregation (DLA) is the process whereby particles
undergoing a random walk due to Brownian motion cluster together to
form aggregates of such particles.
'''

import math
import numpy as np
from __init__ import DLA_generation_dist
import sys
sys.path.append('./')
from utils.plot import scatter_unified_dot_size
from utils.data_conversion.grid.hexagon import (
    convert_indices_to_coordinates as convert_indices_to_coordinates_hexagon,
    convert_coordinates_to_indices as convert_coordinates_to_indices_hexagon,
    dirs as dirs_hexagon
)
from utils.data_conversion.grid.triangle import (
    convert_indices_to_coordinates as convert_indices_to_coordinates_triangle,
    convert_coordinates_to_indices as convert_coordinates_to_indices_triangle,
    dirs as dirs_triangle
)

def calculate_dla_cluster_square(N = 1000):
    max_dist = [0]
    def generate_point(radius) -> tuple[int, int]:
        degree = np.random.uniform(0, 2 * math.pi)
        x_raw, y_raw = radius * math.cos(degree), radius * math.sin(degree)
        x = math.floor(x_raw) if x_raw >= 0 else math.ceil(x_raw)
        y = math.floor(y_raw) if y_raw >= 0 else math.ceil(y_raw)
        return x, y
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    recorded_set = set([(0, 0)])
    x_arr, y_arr = [0], [0]
    def random_walk_and_record():
        boundary = max_dist[0] + max(DLA_generation_dist, max_dist[0])
        bb = boundary ** 2
        x, y = generate_point(radius = boundary)
        while x ** 2 + y ** 2 <= bb:
            if len(x_arr) <= 4:
                for i in range(len(x_arr)):
                    if abs(x_arr[i] - x) + abs(y_arr[i] - y) == 1:
                        recorded_set.add((x, y))
                        x_arr.append(x)
                        y_arr.append(y)
                        max_dist[0] = max(max_dist[0], math.sqrt(x ** 2 + y ** 2))
                        return True
            elif (
                (x, y + 1) in recorded_set or
                (x + 1, y) in recorded_set or
                (x - 1, y) in recorded_set or
                (x, y - 1) in recorded_set
            ):
                recorded_set.add((x, y))
                x_arr.append(x)
                y_arr.append(y)
                max_dist[0] = max(max_dist[0], math.sqrt(x ** 2 + y ** 2))
                return True
            dir = dirs[np.random.randint(4)]
            x, y = x + dir[0], y + dir[1]
        return False
    count = 1
    while count < N:
        if random_walk_and_record():
            count += 1
    return np.array(x_arr), np.array(y_arr)

r'''
A             B
    \     /
       0
       |
       |
       C
'''
def calculate_dla_cluster_hexagon(N = 1000):
    max_dist = [0]
    sqrt3 = math.sqrt(3)
    def generate_point(radius) -> tuple[float, float]:
        degree = np.random.uniform(0, 2 * math.pi)
        x_raw, y_raw = radius * math.cos(degree), radius * math.sin(degree)
        x_raw_indice = x_raw / sqrt3 * 2
        xi = math.floor(x_raw_indice) if x_raw_indice >= 0 else math.ceil(x_raw_indice)
        yi = round(y_raw / 1.5)
        yi = yi - 1 if yi >= 0 else yi + 1
        return convert_indices_to_coordinates_hexagon(xi, yi)
    dirs = dirs_hexagon
    recorded_set = set([(0, 0)])
    x_arr, y_arr = [0], [0]
    def random_walk_and_record():
        boundary = max_dist[0] + max(DLA_generation_dist, max_dist[0])
        bb = boundary ** 2
        x, y = generate_point(radius = boundary)
        xi, yi = convert_coordinates_to_indices_hexagon(x, y)
        while x ** 2 + y ** 2 <= bb:
            dir_ind = (xi + yi) % 2
            if (
                (xi + 1, yi) in recorded_set or
                (xi - 1, yi) in recorded_set or
                dir_ind and ((xi, yi + 1) in recorded_set) or
                not dir_ind and ((xi, yi - 1) in recorded_set)
            ):
                recorded_set.add((xi, yi))
                x_arr.append(x)
                y_arr.append(y)
                max_dist[0] = max(max_dist[0], math.sqrt(x ** 2 + y ** 2))
                return True
            dir = dirs[dir_ind][np.random.randint(3)]
            xi, yi = xi + dir[0], yi + dir[1]
            x, y = convert_indices_to_coordinates_hexagon(xi, yi)
        return False
    count = 1
    while count < N:
        if random_walk_and_record():
            count += 1
    return np.array(x_arr), np.array(y_arr)

r'''
B
  \
   A --- C
     \ /
      O
'''
def calculate_dla_cluster_triangle(N = 1000):
    max_dist = [0]
    sqrt3 = math.sqrt(3)
    def generate_point(radius) -> tuple[float, float]:
        degree = np.random.uniform(0, 2 * math.pi)
        x_raw, y_raw = radius * math.cos(degree), radius * math.sin(degree)
        y_raw_indice = y_raw / sqrt3 * 2
        yi = math.floor(y_raw_indice) if y_raw_indice >= 0 else math.ceil(y_raw_indice)
        x_raw_indice = x_raw + yi / 2
        xi = math.floor(x_raw_indice) if x_raw_indice >= 0 else math.ceil(x_raw_indice)
        return convert_indices_to_coordinates_triangle(xi, yi)
    dirs = dirs_triangle
    recorded_set = set([(0, 0)])
    x_arr, y_arr = [0], [0]
    def random_walk_and_record():
        boundary = max_dist[0] + max(DLA_generation_dist, max_dist[0])
        bb = boundary ** 2
        x, y = generate_point(radius = boundary)
        xi, yi = convert_coordinates_to_indices_triangle(x, y)
        while x ** 2 + y ** 2 <= bb:
            if (
                (xi + 1, yi) in recorded_set or
                (xi - 1, yi) in recorded_set or
                (xi, yi + 1) in recorded_set or
                (xi, yi - 1) in recorded_set or
                (xi + 1, yi + 1) in recorded_set or
                (xi - 1, yi - 1) in recorded_set
            ):
                recorded_set.add((xi, yi))
                x_arr.append(x)
                y_arr.append(y)
                max_dist[0] = max(max_dist[0], math.sqrt(x ** 2 + y ** 2))
                return True
            dir = dirs[np.random.randint(6)]
            xi, yi = xi + dir[0], yi + dir[1]
            x, y = convert_indices_to_coordinates_triangle(xi, yi)
        return False
    count = 1
    while count < N:
        if random_walk_and_record():
            count += 1
    return np.array(x_arr), np.array(y_arr)


def plot_dla_cluster(grid_type = 'square', N = 500, unified_dot_size = 1):
    calculator = calculators[grid_type]
    x_nparr, y_nparr = calculator(N)
    scatter_unified_dot_size(x_nparr, y_nparr, unified_dot_size = unified_dot_size)


if __name__ == '__main__':
    calculators = {
        'square': calculate_dla_cluster_square,
        'hexagon': calculate_dla_cluster_hexagon,
        'triangle': calculate_dla_cluster_triangle
    }
    # following examples are extremetly time consuming
    plot_dla_cluster(grid_type = 'square', N = 10000)
    plot_dla_cluster(grid_type = 'hexagon', N = 10000)
    plot_dla_cluster(grid_type = 'triangle', N = 10000)
