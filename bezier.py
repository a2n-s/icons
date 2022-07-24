#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

Point = np.ndarray[float, float]


def bezier_1(point_0: Point, point_1: Point, *, nb_points: int = 1000) -> np.ndarray:
    curve = []
    x_0, y_0 = point_0
    x_1, y_1 = point_1
    for t in np.linspace(0, 1, nb_points):
        x = x_0 * t + x_1 * (1 - t)
        y = y_0 * t + y_1 * (1 - t)
        curve.append((x, y))
    return np.array(curve)


def bezier_2(point_0: Point, point_1: Point, point_2: Point, *, nb_points: int = 1000) -> np.ndarray:
    curve = []
    steps = np.linspace(0, 1, nb_points)
    first = bezier_1(point_0, point_1, nb_points=1000)
    second = bezier_1(point_1, point_2, nb_points=1000)
    for t, (x_01, y_01), (x_12, y_12) in zip(steps, first, second):
        x = x_01 * t + x_12 * (1 - t)
        y = y_01 * t + y_12 * (1 - t)
        curve.append((x, y))
    return np.array(curve)


A = np.array([0, 0])
B = np.array([1, 0.5])
C = np.array([0.5, 0.5])

plt.style.use("dark_background")

curve = bezier_1(A, B, nb_points=1000)
xs = [x for x, _ in curve]
ys = [y for _, y in curve]
plt.plot(xs, ys)
plt.scatter(*A)
plt.scatter(*B)

curve = bezier_2(A, B, C, nb_points=1000)
xs = [x for x, _ in curve]
ys = [y for _, y in curve]
plt.plot(xs, ys)
plt.scatter(*A)
plt.scatter(*B)
plt.scatter(*C)

plt.show()
