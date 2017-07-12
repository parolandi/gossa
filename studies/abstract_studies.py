import kernels.kernel as krn
import modellers.nla_modeller as mdr
import problems.nla_problem as prb
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
        modeller = mdr.ExplicitNlaModeller(self._func)
        problem = prb.ExplicitNlaProblem(self._spec)
        solver = slv.ExplicitNlaSolver(modeller)
        return modeller, problem, solver


class Study():
    """
    Its single responsibility is to find the solution of a problem by invoking the solver
    for a given problem definition
    """

    def __init__(self, factory):
        modeller, problem, solver = factory.create_study_package()
        self.modeller = modeller
        self._problem = problem
        self._solver = solver

    def set_context(self):
        x = self._problem.get_context()
        self._modeller.set_variable_values(x)

    def execute(self):
        self._solver.solve()

    def get_solution(self):
        return self._solver.get_solution()
