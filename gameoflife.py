"""
The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state,
requiring no further input.
One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
It is Turing complete and can simulate a universal constructor or any other Turing machine.

Rules:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

src: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

import os

import matplotlib.pyplot as plot
import numpy
from PIL import Image

from starters import *

STEPS = ((-1, -1), (-1, 0), (-1, 1),
         (0, -1), (0, 1),
         (1, -1), (1, 0), (1, 1))


def next_generation(matrix):
    """
    :param matrix: a configuration
    :return: the next iteration, a new matrix
    """
    next_gen = numpy.copy(matrix)
    for i in range(len(next_gen)):
        for j in range(len(next_gen[0])):
            count = count_living_neighbours(matrix, i, j)
            if matrix[i][j] == 1 and (count == 2 or count == 3):
                next_gen[i][j] = 1
            elif matrix[i][j] == 0 and count == 3:
                next_gen[i][j] = 1
            else:
                next_gen[i][j] = 0
    return next_gen


def count_living_neighbours(matrix, i, j):
    """
    :return: the number of living neighbours of the element at (i, j) in the matrix
    """
    valid_steps = [(x[0] + i, x[1] + j) for x in STEPS if
                   0 <= x[0] + i < len(matrix) and 0 <= x[1] + j < len(matrix[0])]
    return sum([matrix[x][y] for x, y in valid_steps])


DEF_PATH = "images\\generation_{}.png"


def simulate_iterations(n, matrix):
    """
    :param n: number of generations
    :param matrix: initial configuration
    :return: list of Image objects
    """
    return recursive_helper(1, n, matrix, [])


def recursive_helper(start, end, matrix, imgs):
    if start > end: return imgs
    path = DEF_PATH.format(start)
    # generating the image #
    plot.spy(matrix)
    plot.title("Iteration {}".format(start))
    plot.xticks([])
    plot.yticks([])
    plot.savefig(path)
    ########################
    # loading the image and appending it #
    imgs.append(Image.open(path))
    new_gen = next_generation(matrix)
    return recursive_helper(start + 1, end, new_gen, imgs)


if __name__ == '__main__':
    # find more initial configurations in starters.py #
    initial_config = gosper_glider_gun
    N = 30
    images = simulate_iterations(N, initial_config)

    # saving a gif made up of the images #
    images[0].save("output.gif",
                   format="GIF",
                   append_images=images[1:],
                   save_all=True,
                   duration=150,
                   loop=0)
    ######################################

    # deleting the temp files #
    images = []
    [os.remove(DEF_PATH.format(i)) for i in range(1, N + 1)]
    ############################

    print("done")
