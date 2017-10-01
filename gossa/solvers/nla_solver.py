import gossa.solvers.abstract_solver as slv


class ExplicitNlaSolver(slv.AbstractSolver):

    def __init__(self, modeller):
        super(ExplicitNlaSolver, self).__init__(modeller)

    def solve(self):
        self._x = self._modeller.evaluate_constraints()

    def get_solution(self):
        return self._x
