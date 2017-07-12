import unittest
import studies.abstract_studies as sdy

import tests.test_mocks as mock


class TestStudies(unittest.TestCase):

    def test_study(self):
        aproblem = {"input_factors": ["x1", "x2"],
                 "output_responses": ["y1"],
                 "context": {"x1": 0, "x2": 1.1}}
        afactory = sdy.ExplicitNlaStudyFactory(mock.sum_twice_sum, aproblem)
        astudy = sdy.Study(afactory)
        astudy.set_context()
        astudy.execute()
        actual = astudy.get_solution()
        expected = [1.1, 2.2]
        [self.assertAlmostEqual(left, right, delta = 1e-9) for left, right in zip(actual, expected)]


if __name__ == '__main__':
    unittest.main()
