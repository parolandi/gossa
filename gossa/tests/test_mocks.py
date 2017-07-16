import numpy as np


def sum_twice_sum(x):
    val = x[0]+x[1]
    return np.asarray([val, 2*val])


class NlaModellerMock:

    def __init__(self):
        self._x = None

    @staticmethod
    def set_variable_values(self, x):
        self._x = np.asarray(x)

    @staticmethod
    def evaluate_constraints(self):
        return 2*self._x


class NlaSolverMock:

    def __init__(self, modeller):
        self._modeller = modeller
        self._x = None

    @staticmethod
    def solve(self):
        self._x = self._modeller.evaluate_constrants()

    def get_solution(self):
        return self._x