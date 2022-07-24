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


def bezier_2(point_0: Point, point_1: Point, point_2: Point, *, nb_points: int = 1000):
    xs, ys = [], []
    x_0, y_0 = point_0
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    for t in np.linspace(0, 1, nb_points):
        x_01 = x_0 * t + x_1 * (1 - t)
        y_01 = y_0 * t + y_1 * (1 - t)
        x_12 = x_1 * t + x_2 * (1 - t)
        y_12 = y_1 * t + y_2 * (1 - t)
        xs.append(x_01 * t + x_12 * (1 - t))
        ys.append(y_01 * t + y_12 * (1 - t))
    return xs, ys


A = np.array([0, 0])
B = np.array([1, .5])
C = np.array([.5, .5])

plt.style.use("dark_background")

x, y = bezier_1(A, B, nb_points=1000)
plt.plot(x, y)
plt.scatter(*A)
plt.scatter(*B)

x, y = bezier_2(A, B, C, nb_points=1000)
plt.plot(x, y)
plt.scatter(*A)
plt.scatter(*B)
plt.scatter(*C)

plt.show()
