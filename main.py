import time

import matplotlib.pyplot as plt
import numpy as np


def read_data(random=False, s_size=100):
    _x = [1, 3, 9, 1, 9, 8, 6, 7, 2, 5, 10, 10, 4, 1, 7, 2, 5, 5, 9, 8]
    _y = [10, 3, 2, 7, 8, 9, 7, 4, 8, 1, 4, 8, 7, 0, 3, 5, 5, 9, 8, 9]

    if random:
        _x = np.random.randint(-1000, 1000, s_size)
        _y = np.random.randint(-1000, 1000, s_size)

    return np.array(_x), np.array(_y)


def calc_dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    x, y = read_data(random=True)
    data_size = len(x)
    k = 6
    sample = np.random.choice(data_size, k, replace=False)

    centroids_x = [x[i] for i in sample]
    centroids_y = [y[i] for i in sample]

    colors = np.random.choice(30, k, replace=False)
    data_colors = []
    size = 300

    iteration = 0
    sleep_time = 2
    start_time = time.time()
    converge = False

    real_time_view = True

    while not converge:
        iteration += 1
        if real_time_view:
            plt.scatter(x, y, s=120, c=data_colors if len(data_colors) else 'black')
            plt.scatter(centroids_x, centroids_y, s=size, c=colors)
            plt.xlabel('x value')
            plt.ylabel('y value')
            plt.title(f'Iteration {iteration}')
            plt.show()
        centroid_points = [[] for _ in range(k)]
        data_colors = []
        changed = False
        for _x, _y in zip(x, y):
            dist_min = 1000000
            centroid = 0
            for i, (cx, cy) in enumerate(zip(centroids_x, centroids_y)):
                dist = calc_dist(_x, _y, cx, cy)
                if dist < dist_min:
                    dist_min = dist
                    centroid = i
            centroid_points[centroid].append((_x, _y))
            data_colors.append(colors[centroid])
        for i, centroid in enumerate(centroid_points):
            sum_x = 0
            sum_y = 0
            for c in centroid:
                sum_x += c[0]
                sum_y += c[1]
            new_x = sum_x / len(centroid)
            new_y = sum_y / len(centroid)

            if new_x != centroids_x[i] or new_y != centroids_y[i]:
                centroids_x[i] = new_x
                centroids_y[i] = new_y
                changed = True

        converge = not changed
        if real_time_view:
            time.sleep(sleep_time)

    if not real_time_view:
        plt.scatter(x, y, s=120, c=data_colors if len(data_colors) else 'black')
        plt.scatter(centroids_x, centroids_y, s=size, c=colors)
        plt.xlabel('x value')
        plt.ylabel('y value')
        plt.title(f'Iteration {iteration}')
        plt.show()
        sleep_time = 0

    end_time = time.time()
    print(f'Done after {iteration} iterations.\n'
          f'Computation time {end_time - start_time - sleep_time * iteration}')
