import unittest
import gossa.studies.abstract_studies as sdys
import gossa.studies.nla_study as sdy

import gossa.tests.test_mocks as mock


class TestExplicitNlaStudy(unittest.TestCase):

    def test_all(self):
        aproblem = {"input_factors": ["x1", "x2"],
                 "output_responses": ["y1"],
                 "context": {"x1": 0, "x2": 1.1}}

        afactory = sdys.ExplicitNlaStudyFactory(mock.sum_twice_sum, aproblem)
        astudy = sdy.ExplicitNlaStudy(afactory)
        astudy.set_context()
        astudy.execute()
        actual = list(astudy.get_solution().values())
        expected = [1.1, 2.2]
        [self.assertAlmostEqual(left, right, delta = 1e-9) for left, right in zip(actual, expected)]

        aproblem["context"]["x1"] = 1
        astudy.set_context()
        astudy.execute()
        actual = list(astudy.get_solution().values())
        expected = [2.1, 4.2]
        [self.assertAlmostEqual(left, right, delta = 1e-9) for left, right in zip(actual, expected)]


if __name__ == '__main__':
    unittest.main()
