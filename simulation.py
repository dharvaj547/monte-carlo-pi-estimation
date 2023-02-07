import numpy as np
import matplotlib.pyplot as plt


def plot_points(x, y):
    plt.scatter(x, y)
    plt.show()


def main():
    # trials = int(input("Enter the number of trials: "))
    trials = 10000

    # generate random x and y coordinates
    x = np.random.uniform(-1, 1, trials)
    y = np.random.uniform(-1, 1, trials)

    # calculate the distance of each (x, y) point from origin
    distance = np.sqrt(x ** 2 + y ** 2)

    # count the number of points inside the quarter circle
    inside = distance[distance <= 1].size

    # estimate pi
    pi = 4 * inside / trials

    print(pi)


if __name__ == '__main__':
    main()