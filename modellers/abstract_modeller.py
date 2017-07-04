import abc


class AbstractModeller(abc.ABC):
    """
    Its single responsibility is to evaluate the system of equations.
    One can expect zero, first and second order evaluations: constraints (in the general sense),
    Jacobians and Hessians.
    Future design:
     * instead of having to pass "x", one would pass an "evaluation context"
     * given the constraints, there are various ways the Jacobian and Hessian could be constructed
     * instead of having a single modeller, one could have a set of constraint and Jacobian modellers that simply
        evaluate(), for example
    """

    def __init__(self, func):
        """
        :param func: the function defining the set of constraints
        """
        self._constraints = func
        self._x = None

    @abc.abstractmethod
    def evaluate_constraints(self):
        """
        The main responsibility
        :return: an array of constraint values
        """

    @abc.abstractmethod
    def set_variable_values(self, x):
        """
        Does as it says
        :param x:  an array of variable values
        :return: None
        """
