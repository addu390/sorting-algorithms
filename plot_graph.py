from functools import partial
import timeit
import numpy as np
from matplotlib import pyplot

import external_merge_sort
import generate_input
import merge_sort


def plot_time(func, inputs, repeats, n_tests):
    x, y, y_err = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(i)
        y.append(np.mean(t))
        y_err.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=y_err, fmt='-o', label=func.__name__)


def plot_times(functions, inputs, repeats=3, n_tests=1, file_name=""):
    for func in functions:
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Input")
    pyplot.ylabel("Time [s]")
    if not file_name:
        pyplot.show()
    else:
        pyplot.savefig(file_name)


if __name__ == "__main__":
    def external(input_size):
        print("External Sort: " + str(input_size))
        external_merge_sort.default(input_size)


    def in_memory(input_size):
        print("Merge Sort: " + str(input_size))
        merge_sort.default(input_size)


    def python_sort(input_size):
        print("Python Sort: " + str(input_size))
        input = generate_input.to_memory(input_size)
        input.sort()

    plot_times([external, in_memory, python_sort], [1024, 16384, 131072, 262144, 524288, 1048576, 2097152,
                                                     4194304, 8388608], repeats=3, n_tests=1, file_name="output")
