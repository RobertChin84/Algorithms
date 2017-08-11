import unittest
from ..nelder_mead import *

class TestNelderMead(unittest.TestCase):

    def test_sort_function_mappings(self):
        expected = -4
        x = [0, 1, 2, -4, -3]
        actual = sort_function_mappings(lambda xi: xi**2, x)
        assert actual == expected, "actual {} != expected {}".format(actual, expected)


    def test_sort_function_mappings_multivariable(self):
        expected = [-4, 100]
        x = [[0, 2], [1, 3], [2, 4], [-4, 100], [-3, 3]]
        actual = sort_function_mappings(lambda xi: xi[0]**2 + xi[1]**2, x)
        assert actual == expected, "actual {} != expected {}".format(actual, expected)

    def test_get_convergence(self):
        expected = True
        x = [[0, 0], [0, 0.00001], [0, 0.00003], [0, 0], [0.00000001, 0.00001]]
        actual = get_convergence(lambda xi: xi[0]**2 + xi[1]**2, x)
        assert actual == expected, "actual {} != expected {}".format(actual, expected)