import modellers.abstract_modeller as mdr


class ExplicitNlaModeller(mdr.AbstractModeller):

    def __init__(self, func, names):
        super(ExplicitNlaModeller, self).__init__(func, names)

    def evaluate_constraints(self):
        return self._constraints(self._variable_values)
