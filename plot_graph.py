from functools import partial
import timeit
import numpy as np
from matplotlib import pyplot

import external_merge_sort
import generate_input
import in_memory_merge_sort
from time import time


def plot_time(func, inputs, repeats, n_tests):
    x, y, y_err = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(i)
        y.append(np.mean(t))
        y_err.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=y_err, fmt='-o', label=func.__name__)


def plot_times(functions, inputs, repeats=3, n_tests=1, file_name_prefix=""):
    for func in functions:
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Input")
    pyplot.ylabel("Time [s]")
    if not file_name_prefix:
        pyplot.show()
    else:
        pyplot.savefig(file_name_prefix + str(round(time() * 1000)))


if __name__ == "__main__":
    def external(input_size):
        print("External Sort: " + str(input_size))
        external_merge_sort.with_random_numbers(input_size, chunk_size=10000, input_range=(0, 1000000))


    def in_memory(input_size):
        print("Merge Sort: " + str(input_size))
        in_memory_merge_sort.with_random_numbers(input_size, input_range=(0, 1000000))


    def python_sort(input_size):
        print("Python Sort: " + str(input_size))
        input = generate_input.to_memory(input_size, input_range=(0, 1000000))
        input.sort()


    plot_times([python_sort, external, in_memory], [1024, 16384, 131072, 262144, 524288, 1048576, 2097152,
                                                    4194304, 8388608], repeats=3, n_tests=1, file_name_prefix="output-")
