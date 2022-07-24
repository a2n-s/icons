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


def bezier_3(point_0: Point, point_1: Point, point_2: Point, point_3: Point, *, nb_points: int = 1000) -> np.ndarray:
    curve = []
    steps = np.linspace(0, 1, nb_points)
    first = bezier_2(point_0, point_1, point_2, nb_points=1000)
    second = bezier_2(point_1, point_2, point_3, nb_points=1000)
    for t, (x_01, y_01), (x_12, y_12) in zip(steps, first, second):
        x = x_01 * t + x_12 * (1 - t)
        y = y_01 * t + y_12 * (1 - t)
        curve.append((x, y))
    return np.array(curve)


def test(function, *, nb_control_points: int, color: str, nb_points: int):
    control_points = [np.random.uniform(0, 1, size=(2,)) for _ in range(nb_control_points)]
    x, y = function(*control_points, nb_points=nb_points).transpose()
    plt.plot(x, y, c=color)
    for control in control_points:
        plt.scatter(*control, c=color)


def main(*, nb_points: int):
    plt.style.use("dark_background")

    test(bezier_1, nb_control_points=2, color="green", nb_points=nb_points)
    test(bezier_2, nb_control_points=3, color="red", nb_points=nb_points)
    test(bezier_3, nb_control_points=4, color="blue", nb_points=nb_points)

    plt.show()


if __name__ == '__main__':
    NB_POINTS = 1000

    main(nb_points=NB_POINTS)
