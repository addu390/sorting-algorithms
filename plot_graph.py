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
        x.append(len(i))
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
    input_1 = generate_input.to_memory(5, (0, 10))
    input_2 = generate_input.to_memory(6, (0, 10))
    input_3 = generate_input.to_memory(7, (0, 10))

    def external_in_memory_input(input_list):
        print("External Sort: " + str(len(input_list)))
        external_merge_sort.list_sort(input_list=input_list, chunk_size=100000)


    def external_file_input(input_size, chunk_size, input_range):
        print("External Sort (File Input): " + str(input_size))
        external_merge_sort.generate_and_sort(input_size=input_size, chunk_size=chunk_size, input_range=input_range)


    def in_memory_merge(input_list):
        print("Merge Sort: " + str(len(input_list)))
        in_memory_merge_sort.list_sort(input_list=input_list)


    def in_memory_tim(input_list):
        print("Python Sort: " + str(len(input_list)))
        sorted(input_list)

    plot_times([external_in_memory_input, in_memory_merge, in_memory_tim],
               [generate_input.to_memory(input_size=524288, input_range=(0, 1000000)),
                generate_input.to_memory(input_size=1048576, input_range=(0, 1000000)),
                generate_input.to_memory(input_size=2097152, input_range=(0, 1000000)),
                generate_input.to_memory(input_size=4194304, input_range=(0, 1000000))],
               repeats=2, n_tests=1, file_name_prefix="output-")
