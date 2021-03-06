import abc
import numpy as np
import gossa.modellers.nla_modeller as mdr
import gossa.problems.nla_problem as prb
import gossa.problems.abstract_problem as prbs
import gossa.solvers.nla_solver as slv


class ExplicitNlaStudyFactory():
    def __init__(self, func, spec):
        """
        :param func: the function to wrap in the modeller
        :param spec: the specification to instantiate the problem
        """
        self._func = func
        self._spec = spec

    def create_study_package(self):
        problem = prb.ExplicitNlaProblem(prbs.ProblemFactory(self._spec))
        modeller = mdr.ExplicitNlaModeller(self._func, problem.input_factors)
        solver = slv.ExplicitNlaSolver(modeller)
        return modeller, problem, solver


class AbstractStudy(abc.ABC):
    """
    Its single responsibility is to find the solution of a problem by invoking the solver
    for a given problem definition
    """

    def __init__(self, factory):
        modeller, problem, solver = factory.create_study_package()
        self._modeller = modeller
        self._problem = problem
        self._solver = solver
        self._solution = None

    def set_context(self):
        context = self._problem.context
        x = np.asarray(list(context.values()))
        self._modeller.set_variable_values(x)

    def execute(self):
        self._solver.solve()

    def get_solution(self):
        self._put_solution()
        return self._solution.get_solution()

    @abc.abstractmethod
    def _put_solution(self):
        """
        Construct the solution depending on the type of study
        :return: a solution object
        """

