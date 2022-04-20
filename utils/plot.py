import matplotlib.pyplot as plt
import numpy as np

def scatter_unified_dot_size(x_nparr, y_nparr, unified_dot_size = 0.8):
    print(len(x_nparr), len(y_nparr))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    plt.scatter(x_nparr, y_nparr, s = np.array([unified_dot_size] * len(x_nparr)))
    plt.show()
