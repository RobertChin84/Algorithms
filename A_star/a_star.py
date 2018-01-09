"""
This script will handle the algorithm for A* algorithm as described here
https://en.wikipedia.org/wiki/A*_search_algorithm

REquires python 3+
"""
from itertools import product
from numpy import Infinity
from sys import maxsize

# TODO: 
class Point(object):
    id = 0

    def __init__(self, x, y, id, data=None):
        self.x = x
        self.y = y
        self.data = data
        self.f = Infinity
        self.g = Infinity
        self.h = 0
        self.id = id
        self.previous = None
        self.neighbours = []

    def __mul__(self, p2):
        return self.x * p2.x + self.y*p2.y

    def __sub__(self, p2):
        """
        compute the manhatten distance between two points on a grid
        :param p2:
        :return:
        """
        return abs(self.x - p2.x) + abs(self.y-p2.y)

    def get_coords(self):
        return [self.x, self.y]

    def set_neighbours(self, p2):
        self.neighbours.append(p2)


class Grid(object):

    def __init__(self, points):
        self.points = points
        self.height = len(points)
        self.width = len(points[0])
        self.grid = None
        self.compute_neighbours()

    def compute_neighbours(self):
        def update_neighbours(row_index, col_index , point):
            for k in product([-1, 0, 1], repeat=2):
                if k != (0, 0):
                    n_col_index = col_index + k[1]
                    n_row_index = row_index + k[0]

                    if 0 <= n_col_index < self.width and 0 <= n_row_index < self.height:
                        point.set_neighbours(self.points[n_row_index][n_col_index])
            return point
        self.grid = [[update_neighbours(i, j, p) for j, p in enumerate(row)] for i, row in enumerate(self.points)]

    def print_grid(self):
        for row in self.grid:
            print(' '.join(['({}, {})'.format(r.data, r.id) for r in row]))

    def print_neighbours(self):
        max_
        for row in self.grid:
            for r in row:

                print('id: {}'.format(r.id), ' '.join([str(n.id) for n in r.neighbours]))

    def get_point(self, indices):
        row_index, col_index = indices
        return self.grid[row_index][col_index]


def generate_point_matrix(filename=None):
    """
    This function reads the text file to generate a list of lists of chars i.e. 'o','x'.
    :param filename:
    :return:
        data: [['o','x','o'],['o','o','o']]
    """
    nums = iter(range(maxsize))
    assert filename
    k = 1
    with open(filename, 'r') as f:

        data = [[Point(i, j, next(nums), r)
                for (j, r) in enumerate(row.strip())]
                for (i, row) in enumerate(f.readlines())]
    return data


def euclid_distance(p1, p2):
    """
    Compute the Euclid distance (x^2+y^2)^0.5
    :param p1:
    :param p2:
    :return:
       dist
    """
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5


def get_min_f_score_value(open_set):
    min_node = None
    min_f_score = Infinity
    for node in open_set:

        if node.f < min_f_score:
            min_node = node
            min_f_score = node.f
    return min_node


def compute_heuristic_cost(curr, end, metric='euclid'):
    """
    Compute the g(n) between the current point and the desired end node
    :param curr: Point class
    :param end: Point class
    :param metric: type of distance calculation
    :return:
       dist
    """
    if metric == 'euclid':
        return euclid_distance(curr, end)
    if metric == 'manhattan':
        return curr - end


def reconstruct_path(path_map, start, end):
    """
    Reconstruct path allows for the path map containing the edges (pairings of current and neighbour nodes) is parsed
    to reveal the optimal path through a grid.
    :param path_map: dictionary of neighbour and next node
    :param start: starting node
    :param end: last node
    :return:
    """
    current = path_map[end.id]
    path = [end]
    while start != current:
        path.append(current)
        current = path_map[current.id]
    path.append(start)
    return reversed(path)


def A_star(start_point, end_point, grid):
    """
    A* algorithm allows for a path to be generated through a grid system to an objective point in the 2d space. The
    algorithm will try all nodes upto a heuristic.
    :param start_point:
    :param end_point:
    :param grid:
    :return:
    """
    # Initialise the scores for which we will use to determine the best route
    closed_set = set()
    open_set = set()
    came_from = {}

    # get the start and end node
    start = grid.get_point(start_point)
    goal = grid.get_point(end_point)

    # set the f & g start values
    start.g = 0.0
    start.f = start.g + compute_heuristic_cost(start, goal)
    open_set.add(start)

    # while we have valid nodes to check
    while len(open_set) > 0:
        current = get_min_f_score_value(open_set)
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        # finished with current node
        open_set.remove(current)
        closed_set.add(current)

        for neighbour in current.neighbours:
            # check if the 'new' neighbour node is in the closed_set if so
            # then ignore
            if neighbour in closed_set or neighbour.data == 'x':
                continue

            # compute the temp g score of previous plus distance between current and neighbour
            temp_g_score = current.g + compute_heuristic_cost(current, neighbour)
            # add new neighbour to be checked in the next round
            if neighbour not in open_set:
                open_set.add(neighbour)
                # set the path
                if temp_g_score < neighbour.g:
                    # update the g score
                    neighbour.g = temp_g_score
                    came_from[neighbour.id] = current

                neighbour.h = compute_heuristic_cost(goal, neighbour)
                neighbour.f = neighbour.g + neighbour.h
    return None


if __name__ == "__main__":
    points = generate_point_matrix('./resources/matrix_test.txt')
    print('Size of grid: {} x {}'.format(len(points), len(points[0])) )
    grid = Grid(points)
    start = [0,0]
    end = [4, 4]
    grid.print_grid()
    #grid.print_neighbours()
    actual_came_from = A_star(start, end, grid)
    print("*" * 40)
    print("Output ids for the route")
    print("*" * 40)
    print([n.id for n in actual_came_from])



