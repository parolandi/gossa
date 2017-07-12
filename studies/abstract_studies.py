import numpy as np
import modellers.nla_modeller as mdr
import problems.nla_problem as prb
import problems.abstract_problem as prbs
import solvers.nla_solver as slv


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


class Study():
    """
    Its single responsibility is to find the solution of a problem by invoking the solver
    for a given problem definition
    """

    def __init__(self, factory):
        modeller, problem, solver = factory.create_study_package()
        self._modeller = modeller
        self._problem = problem
        self._solver = solver

    def set_context(self):
        context = self._problem.context
        x = np.asarray(list(context.values()))
        self._modeller.set_variable_values(x)

    def execute(self):
        self._solver.solve()

    def get_solution(self):
        return self._solver.get_solution()
