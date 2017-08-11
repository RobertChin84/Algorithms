"""
A Nelder-Mead implementation to compute the optimal solution for a nonlinear constraint problem
"""
import numpy as np


def sort_function_mappings(f, x):
    """
    Sort function mapping f(x1) < f(x2) < f(xn)
    To get the worse value corresponding to the largest f
    :param f:
    :param x:
    :return:
    """
    f_values = list(map(f, list(x)))
    fs = np.argsort(f_values)
    return x[fs[-1]]


def get_convergence(f, x, tol=0.0000005):
    f_values = list(map(f, list(x)))
    return max(f_values) - min(f_values) < tol


def nelder_mead(x, alpha, gamma, f):
    """

    :param x:
    :param alpha: > 0
    :param gamma: > 1
    :param f: function to be optimised
    :return:
    """
    is_converged = False

    while not is_converged:
        is_converged = get_convergence(f, x)
        # compute the minimum f f(x1) < f(x2) < f(xn)
        x[-1] = sort_function_mappings(f, x)

        # compute centroid except the last point
        x0 = np.mean(x[:-1])

        # compute reflected points
        xr = x0 + alpha * (x0 - x[-1])
        f_r = f(xr)
        if f(x[0]) <= f_r < f(x[-2]):
            # replace the last point with reflected point
            x[-1] = xr
            continue
        # expansion phase
        if f_r < x[0]:
            xe = x0 + gamma * (xr - x0)






