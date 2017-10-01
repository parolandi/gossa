import unittest
import gossa.kernels.kernel as kern

import gossa.tests.test_mocks as mock


class TestKernel(unittest.TestCase):

    def test_all(self):
        afactory = kern.ExplicitNlaKernelFactory(mock.sum_twice_sum, ["x1", "x2"])
        akernel = kern.Kernel(afactory)
        akernel.set_values([1, 2])
        akernel.compute()
        actual = akernel.get_solution()
        expected = [3, 6]
        [self.assertAlmostEqual(left, right, delta=1E-3) for left, right in zip(actual, expected)]


if __name__ == '__main__':
    unittest.main()
