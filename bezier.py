#!/usr/bin/env python3

from typing import List

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


def bezier(*points: List[Point], nb_points: int = 1000) -> np.ndarray:
    if len(points) < 2:
        raise ValueError("Not enough control points given...")

    if len(points) == 2:
        return bezier_1(*points, nb_points=nb_points)

    curve = []
    steps = np.linspace(0, 1, nb_points)
    first = bezier(*points[:-1], nb_points=nb_points)
    second = bezier(*points[1:], nb_points=nb_points)
    for t, (x_first, y_first), (x_second, y_second) in zip(steps, first, second):
        x = x_first * t + x_second * (1 - t)
        y = y_first * t + y_second * (1 - t)
        curve.append((x, y))
    return np.array(curve)


def test(function, *, nb_control_points: int, color: str, nb_points: int):
    control_points = [np.random.uniform(0, 1, size=(2,)) for _ in range(nb_control_points)]
    x, y = function(*control_points, nb_points=nb_points).transpose()
    plt.plot(x, y, c=color)
    plt.plot(*np.array(control_points).transpose(), c=color, linestyle="-.", linewidth=.2, marker="+")


def main(*, nb_points: int):
    plt.style.use("dark_background")

    test(bezier, nb_control_points=2, color="cyan", nb_points=nb_points)
    test(bezier, nb_control_points=3, color="green", nb_points=nb_points)
    test(bezier, nb_control_points=4, color="yellow", nb_points=nb_points)
    test(bezier, nb_control_points=5, color="red", nb_points=nb_points)
    test(bezier, nb_control_points=6, color="magenta", nb_points=nb_points)

    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    NB_POINTS = 1000

    main(nb_points=NB_POINTS)
