import abc
import numpy as np


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

    def __init__(self, func, names):
        """
        :param func: the function defining the set of constraints
        :param names: the variable names
        """
        self._constraints = func
        self._variables = names
        self._variable_values = self._set_initial_variable_values()

    @abc.abstractmethod
    def evaluate_constraints(self):
        """
        The main responsibility
        :return: an array of constraint values
        """

    @property
    def variable_values(self):
        return self._variable_values

    #@variable_values.setter
    def set_variable_values(self, x):
        """
        :param x:  an array of variable values
        :return: None
        """
        self._variable_values = x

    @property
    def variable_names(self):
        return self._variables


    def _set_initial_variable_values(self):
        return np.zeros(len(self._variables))
