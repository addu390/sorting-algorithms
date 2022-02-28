from functools import partial
import timeit
import numpy as np
from matplotlib import pyplot

import external_sort
import file_util
import merge_sort
from time import time


def plot_time(func, inputs, repeats, n_tests):
    x, y, y_err = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(i[0])
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

    def generate(input_size, input_range, input_file, output_file):
        file_util.to_file(input_size, input_range, input_file)
        return input_size, input_file, output_file


    def external_merge(inputs):
        print("External Sort: " + str(inputs[0]))
        external_sort.sort_from_file(inputs[0], inputs[1], inputs[2], chunk_size=100000)


    def in_memory_merge(inputs):
        print("Merge Sort: " + str(inputs[0]))
        merge_sort.sort_from_file(inputs[0], inputs[1], inputs[2])


    def in_memory_tim(inputs):
        print("Python Sort: " + str(inputs[0]))
        input = file_util.from_file(inputs[1])
        file_util.list_to_file(sorted(input), inputs[2])

    upper_limit = 1000000
    plot_times([in_memory_tim, external_merge, in_memory_merge],
               [generate(input_size=262144, input_range=(0, upper_limit), input_file="input-0.csv", output_file="output-0.csv"),
                generate(input_size=1048576, input_range=(0, upper_limit), input_file="input-1.csv", output_file="output-1.csv"),
                generate(input_size=2097152, input_range=(0, upper_limit), input_file="input-2.csv", output_file="output-2.csv"),
                generate(input_size=8388608, input_range=(0, upper_limit), input_file="input-3.csv", output_file="output-3.csv"),
                generate(input_size=16777216, input_range=(0, upper_limit), input_file="input-4.csv", output_file="output-4.csv")],
               repeats=1, n_tests=1, file_name_prefix="plot-")
