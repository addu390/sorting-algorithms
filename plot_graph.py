from functools import partial
import timeit
import numpy as np
from matplotlib import pyplot

import external_merge_sort
import merge_sort


def plot_time(func, inputs, repeats, n_tests):
    """
    Run timer and plot time complexity of `func` using the iterable `inputs`.

    Run the function `n_tests` times per `repeats`.
    """
    x, y, yerr = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(i)
        y.append(np.mean(t))
        yerr.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=yerr, fmt='-o', label=func.__name__)


def plot_times(functions, inputs, repeats=3, n_tests=1, file_name=""):
    """
    Run timer and plot time complexity of all `functions`,
    using the iterable `inputs`.

    Run the functions `n_tests` times per `repeats`.

    Adds a legend containing the labels added by `plot_time`.
    """
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
    def external(n):
        external_merge_sort.sample(n)


    def in_memory(n):
        merge_sort.sample(n)


    plot_times([in_memory, external], [262144, 524288, 1048576, 2097152, 4194304, 8388608], repeats=1)
