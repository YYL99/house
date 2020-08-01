# -*- coding: utf-8 -*-

import random
from random import choice
import matplotlib.pyplot as plt
import numpy as np


class RandomWalk1:
    def __init__(self):
        self.position = 0

    def walk(self):
        walk = [self.position]
        steps = 1000
        for i in range(steps):
            step = 1 if random.randint(0, 1) else -1
            self.position += step
            walk.append(self.position)

        x = np.arange(0, 1001, 1)
        plt.xlim(0, 100)
        plt.ylim(-5, 20)    # 由于生成是随机的，因此纵轴的范围不可控
        plt.plot(x, walk)
        plt.legend()
        plt.show()


class RandomWalk2:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction*x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction*y_distance

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)


class RandomWalkMany:
    def __init__(self):
        self.walks = 5000
        self.steps = 1000

    def walk(self):
        draws = np.random.randint(0, 2, size=(self.walks, self.steps))
        steps = np.where(draws > 0, 1, -1)
        walks = steps.cumsum(1)
        hits30 = (np.abs(walks) >= 30).any(1)
        crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
        print(hits30.sum(), crossing_times.mean())
        # 每一行为一个随机漫步


if __name__ == '__main__':
    while False:
        rw = RandomWalk2()
        rw.fill_walk()
        plt.figure(figsize=(15, 8))
        point_numbers = list(range(rw.num_points))
        # scatter散点图
        plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers,
                    edgecolor='none', cmap=plt.cm.Blues)

        plt.scatter(rw.x_values[0], rw.y_values[0], s=50,
                    edgecolor='none',c='green')

        plt.scatter(rw.x_values[-1], rw.y_values[-1], s=50,
                    edgecolor='none',c='green')

        plt.show()

        a = input("do you want to walk again?(y/n)")
        if a == 'n':
            break
    RandomWalk1().walk()
