import unittest
from ..a_star import Point, generate_point_matrix, Grid, A_star


class TestAstarAlgo(unittest.TestCase):

    def test_Point_class_multiplying(self):
        p1 = Point(2, 5, 'x')
        p2 = Point(2, 5, 'a')
        expected = 29
        actual = p1*p2
        assert actual == expected, "actual {} != expected {}".format(actual, expected)

    def test_Point_class_subtracting(self):
        p1 = Point(0, 0, 0, 'x')
        p2 = Point(3, 3, 1, 'a')
        expected = 6
        actual = p1-p2
        assert actual == expected, "actual {} != expected {}".format(actual, expected)

    def test_data_matrix(self):
        expected = [[Point(0, 0, 0, 'o'), Point(0, 1, 'o')],
                    [Point(1, 0, 1, 'x'), Point(1, 1, 'o')]]

        actual = generate_point_matrix('test_matrix_1.txt')

        expected = [[ele.data for ele in row] for row in expected]
        actual = [[ele.data for ele in row] for row in actual]

        assert actual == expected, "actual {} != expected {}".format(actual, expected)

    def test_grid_generator(self):
        points = [[Point(0, 0, 0, 'o'), Point(0, 1, 1, 'o')],
                  [Point(1, 0, 2, 'x'), Point(1, 1, 3, 'o')]]
        grid = Grid(points).grid
        expected = [[0, 1], [1, 0], [1, 1]]
        actual = [p.get_coords() for p in grid[0][0].neighbours]
        assert sorted(actual) == sorted(expected), "actual {} != expected {}".format(actual, expected)

    def test_A_star(self):
        points = [[Point(0, 0, 0, 'o'), Point(0, 1, 1, 'o')],
                  [Point(1, 0, 2, 'x'), Point(1, 1, 3, 'o')]]
        grid = Grid(points)
        start = [0, 0]
        end = [1, 1]
        expected_route = [[0,0], [0, 1], [1, 1]]
        actual_came_from = A_star(start, end, grid)
        actual_route = [v.get_coords() for k, v in actual_came_from.iteritems()]
        assert actual_route == expected_route, "actual {} != expected {}".format(actual_route, expected_route)
