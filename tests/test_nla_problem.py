import unittest
import problems.nla_problem as prb

import problems.abstract_problem as aprb


class TestExplicitNlaProblem(unittest.TestCase):

    def test_construct_get_set(self):
        aspec = {"input_factors": ["one", "two"], "output_responses": ["three", "four"]}
        afactory = aprb.ProblemFactory(aspec)
        nla_problem = prb.ExplicitNlaProblem(afactory)
        self.assertTrue(len(nla_problem.input_factors) == 2)
        self.assertTrue(len(nla_problem.output_responses) == 2)
        self.assertTrue(nla_problem.decision_variables is None)
        self.assertTrue(nla_problem.objective_functions is None)
        self.assertTrue(nla_problem.model_coefficients is None)


if __name__ == '__main__':
    unittest.main()
