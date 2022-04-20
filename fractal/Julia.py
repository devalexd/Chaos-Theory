r'''
A very popular complex dynamical system is given by the family of
complex quadratic polynomials, a special case of rational maps.
Such quadratic polynomials can be expressed as:
f_c(z) = z^2 + c
where c is a complex parameter.
Fix some R > 0 large enough that R^2 - R >= |c|.
Then the filled Julia set for this system is the subset of the
complex plane given by:
K(f_c) = {z -> C: any n -> N, |f_c^n(z)| <= R},
where f_c^n(z) is the n-th iterate of f_c(z).
The Julia set J(f_c) of this function is the boundary of K(f_c).
'''

import math
import numpy as np
from __init__ import delta
import sys
sys.path.append('./')
from utils.plot import scatter_unified_dot_size

# c -> a + bi
def calculate_julia_set(a, b, delta = delta, iterations = 50):
    c = 0.5 + math.sqrt(1 + 4 * math.sqrt(a ** 2 + b ** 2)) / 2
    cc = c ** 2
    def validate(x, y):
        for _ in range(iterations):
            x, y = x ** 2 - y ** 2 + a, 2 * x * y + b
            if x ** 2 + y ** 2 > cc: return False
        return True
    x_arr, y_arr = [], []
    for xi in np.arange(delta - c, c, delta):
        y = math.sqrt(cc - xi * xi)
        for yi in np.arange(delta - y, y, delta):
            if validate(xi, yi):
                x_arr.append(xi)
                y_arr.append(yi)
    x_nparr, y_nparr = np.array(x_arr), np.array(y_arr)
    return x_nparr, y_nparr

def plot_julia_set(a, b, delta = delta, iterations = 50, unified_dot_size = 0.5):
    x_nparr, y_nparr = calculate_julia_set(a, b, delta, iterations)
    scatter_unified_dot_size(x_nparr, y_nparr, unified_dot_size = unified_dot_size)


if __name__ == '__main__':
    # following examples are extremetly time consuming
    plot_julia_set(0.11, 0.66, delta = 0.0003)
    plot_julia_set(0, 1, delta = 0.000001)