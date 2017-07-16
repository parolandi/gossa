import gossa.studies.abstract_studies as sdy
import gossa.solutions.nla_solution as sln


class ExplicitNlaStudy(sdy.AbstractStudy):

    def __init__(self, factory):
        super(ExplicitNlaStudy, self).__init__(factory)

    def _put_solution(self):
        y = self._solver.get_solution()
        self._solution = sln.ExplicitNlaSolution(self._problem._output_responses)
        self._solution.set_variable_values(y)

