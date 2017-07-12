class ExplicitNlaSolution():

    def __init__(self, names):
        """
        :param names: the names of the variables
        """
        self._names = names

    def set_variable_values(self, x):
        self._values = x

    def get_solution(self):
        """
        The main responsibility.
        :return: dictionary of variable value pairs
        """
        return {key: val for key, val in zip(self._names, self._values)}
    