import problems.abstract_problem as prb


class ExplicitNlaProblem(prb.Problem):

    def _init__(self, factory):
        super(ExplicitNlaProblem, self).__init__(factory)
