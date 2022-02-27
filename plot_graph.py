from functools import partial
import timeit
import numpy as np
from matplotlib import pyplot

import external_sort
import file_util
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
    input_file_name = "unsorted.csv"

    def generate(input_size, input_range):
        file_util.to_file(input_size, input_range, input_file_name)
        return input_size


    def external(input_size):
        print("External Sort: " + str(input_size))
        external_sort.sort_from_file(input_file_name, input_size, chunk_size=100000)


    def in_memory(input_size):
        print("Merge Sort: " + str(input_size))
        in_memory_merge_sort.sort_from_file(input_file_name, input_size)


    def python_sort(input_size):
        print("Python Sort: " + str(input_size))
        input = file_util.from_file(input_file_name)
        print(len(input))
        sorted(input)

    plot_times([python_sort, external, in_memory],
               [generate(131072, input_range=(0, 1000000)),
                generate(262144, input_range=(0, 1000000)),
                generate(524288, input_range=(0, 1000000)),
                generate(1048576, input_range=(0, 10000000)),
                generate(4194304, input_range=(0, 10000000))],
               repeats=3, n_tests=1, file_name_prefix="output-")
