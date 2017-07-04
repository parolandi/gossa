import modellers.abstract_modeller as mdr


class ExplicitNlaModeller(mdr.AbstractModeller):

    def __init__(self, func):
        super(ExplicitNlaModeller, self).__init__(func)

    def set_variable_values(self, x):
        self._x = x

    def evaluate_constraints(self):
        return self._constraints(self._x)