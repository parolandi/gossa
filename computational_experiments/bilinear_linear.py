import studies.nla_study as sdy
import studies.abstract_studies as sdys
import models.bilinear_linear as mdl


def bilinear_linear_1():
    problem = {"input_factors": ["x1", "x2"],
               "output_responses": ["y1", "y2"],
               "context": {"x1": 0.0, "x2": 0.0}}
    factory = sdys.ExplicitNlaStudyFactory(mdl.bilinear_linear, problem)
    study = sdy.ExplicitNlaStudy(factory)
    study.set_context()
    study.execute()
    return study.get_solution()


if __name__ == '__main__':
    solution = bilinear_linear_1()
    print(solution)