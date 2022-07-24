#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

Point = np.ndarray[float, float]


def bezier_1(point_0: Point, point_1: Point, *, nb_points: int = 1000):
    xs, ys = [], []
    x_0, y_0 = point_0
    x_1, y_1 = point_1
    for t in np.linspace(0, 1, nb_points):
        xs.append(x_0 * t + x_1 * (1 - t))
        ys.append(y_0 * t + y_1 * (1 - t))
    return xs, ys


A = np.array([0, 0])
B = np.array([1, .5])

x, y = bezier_1(A, B, nb_points=1000)

plt.style.use("dark_background")
plt.plot(x, y)
plt.show()
