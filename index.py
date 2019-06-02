import numpy as np


def test():
    world = np.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str)
    print(type(world))
    # print(world)
    # print(help(numpy.genfromtxt))
    vector = np.array([5, 6, 7, 8, 9])
    print(vector)
    result = (vector == 8)
    print(result)
    print(vector[result])


if __name__ == '__main__':
    test()
