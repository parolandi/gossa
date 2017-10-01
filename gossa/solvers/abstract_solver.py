import abc


class AbstractSolver(abc.ABC):
    """
    Its single responsibility is to solve the system of equations.
    """

    def __init__(self, modeller):
        """
        :param modeller: the AbstractModeller
        """
        self._modeller = modeller
        self._x = None

    @abc.abstractmethod
    def solve(self):
        """
        The main responsibility
        :return: None
        """

    @abc.abstractmethod
    def get_solution(self):
        """
        Get the variable values that correspond to the solution
        If a solution is not found, get variable values that correspond
        to a contract defined by the solver (e.g., best attempt, failure point, etc)
        :return: a numpy array
        """