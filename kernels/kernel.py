import kernels.abstract_kernel as krn
import modellers.nla_modeller as mdr
import solvers.nla_solver as slv


class ExplicitNlaKernelFactory(krn.AbstractKernelFactory):

    def __init__(self, func, names):
        super(ExplicitNlaKernelFactory, self).__init__(func, names)

    def create_kernel_package(self):
        modeller = mdr.ExplicitNlaModeller(self._func, self._names)
        solver = slv.ExplicitNlaSolver(modeller)
        return modeller, solver


class Kernel():
    """
    As an abstraction, a kernel presents a complex systems of equations as a simple function evaluation
    """

    def __init__(self, factory):
        self._modeller, self._solver = factory.create_kernel_package()

    def set_values(self, x):
        self._modeller.set_variable_values(x)

    def compute(self):
        self._solver.solve()

    def get_solution(self):
        return self._solver.get_solution()

