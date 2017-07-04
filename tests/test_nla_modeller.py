import unittest
import modellers.nla_modeller as mdr

import tests.test_mocks as mock


class TestExplicitNlaModeller(unittest.TestCase):

    def test_evaluate_constraints(self):
        modeller = mdr.ExplicitNlaModeller(mock.sum_twice_sum)
        modeller.set_variable_values([0, 1])
        actual = modeller.evaluate_constraints()
        expected = [1, 2]
        [self.assertAlmostEqual(left, right)
            for left, right in zip(actual, expected)]


if __name__ == '__main__':
    unittest.main()
