class ProblemFactory():
    """
    Interpret the problem formulation from a dictionary
    Future: use json/yaml
    """

    def __init__(self, spec):
        """
        :param spec: the formulation in a domain-specific language (dsl)
        """
        self._input_factors = spec["input_factors"]
        self._output_responses = spec["output_responses"]
        self._context = spec["context"]


class Problem():
    """
    Its single responsibility is to formulate a given domain-specific problem
    Future: this "contextualized" domain-specific problem will be matched with the corresponding
        "pure" mathematical problem
    """

    def __init__(self, factory):
        """
        :param factory: the problem factory that contains the problem definition
        """
        # system's disturbances, sources of variability or uncertainty
        self._input_factors = factory._input_factors
        # system's performance indicators
        self._output_responses = factory._output_responses
        # system's design and control variables
        self._decision_variables = None
        # system's key performance indicators
        self._objective_functions = None
        # model's sources of uncertainty (i.e., due to modeling, not to the system)
        self._model_coefficients = None
        # parameterization context
        self._context = factory._context

    @property
    def input_factors(self):
        return self._input_factors

    @property
    def output_responses(self):
        return self._output_responses

    @property
    def decision_variables(self):
        return self._decision_variables

    @property
    def objective_functions(self):
        return self._objective_functions

    @property
    def model_coefficients(self):
        return self._model_coefficients

    @property
    def context(self):
        return self._context

