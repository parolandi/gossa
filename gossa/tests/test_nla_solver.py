import unittest
import gossa.solvers.nla_solver as slv

import gossa.modellers.nla_modeller as mdr
import gossa.tests.test_mocks as mock


class TestExplicitNlaSolver(unittest.TestCase):

    def test_solve(self):

        nla_modeller = mdr.ExplicitNlaModeller(mock.sum_twice_sum, ["x1", "x2"])
        nla_modeller.set_variable_values([0, 1])
        nla_solver = slv.ExplicitNlaSolver(nla_modeller)
        nla_solver.solve()
        actual = nla_solver.get_solution()
        expected = [1, 2]
        [self.assertAlmostEqual(left, right, delta=1E-3)
            for left, right in zip(actual, expected)]


if __name__ == '__main__':
    unittest.main()
