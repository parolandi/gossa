import unittest
import gossa.problems.nla_problem as prb

import gossa.problems.abstract_problem as aprb


class TestExplicitNlaProblem(unittest.TestCase):

    def setUp(self):
        self._aspec = {"input_factors": ["x1", "x2"],
                 "output_responses": ["y1", "y2"],
                 "context": {"x1": 0, "x2": 1.1}}
        self._afactory = aprb.ProblemFactory(self._aspec)

    def test_construct_get(self):
        nla_problem = prb.ExplicitNlaProblem(self._afactory)
        self.assertTrue(len(nla_problem.input_factors) == 2)
        self.assertTrue(len(nla_problem.output_responses) == 2)
        self.assertTrue(nla_problem.decision_variables is None)
        self.assertTrue(nla_problem.objective_functions is None)
        self.assertTrue(nla_problem.model_coefficients is None)
        self.assertTrue(len(nla_problem.context) == 2)

    def test_context(self):
        nla_problem = prb.ExplicitNlaProblem(self._afactory)
        context = nla_problem.context
        self.assertEqual(0, context["x1"])
        self.assertAlmostEqual(1.1, context["x2"], delta = 1e-9)


if __name__ == '__main__':
    unittest.main()
