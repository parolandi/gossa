import unittest
import modellers.nla_modeller as mdr

import tests.test_mocks as mock


class TestExplicitNlaModeller(unittest.TestCase):

    def test_evaluate_constraints(self):
        modeller = mdr.ExplicitNlaModeller(mock.sum_twice_sum, ["x1", "x2"])
        modeller.set_variable_values([0, 1])
        actual = modeller.evaluate_constraints()
        expected = [1, 2]
        [self.assertAlmostEqual(left, right)
            for left, right in zip(actual, expected)]

    def test_getters(self):
        modeller = mdr.ExplicitNlaModeller(mock.sum_twice_sum, ["x1", "x2"])
        self.assertTrue(len(modeller.variable_names) == 2)
        self.assertTrue(len(modeller.variable_values) == 2)


if __name__ == '__main__':
    unittest.main()
