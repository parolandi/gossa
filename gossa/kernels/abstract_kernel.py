import abc


class AbstractKernelFactory(abc.ABC):
    """
    Its single responsibility is to create a "package" that offers a modeller-solver
    combo of a concrete type (e.g., NLA)
    """

    def __init__(self, func, names):
        """
        :param func: the function that will be used by the modeller
        """
        self._func = func
        self._names = names

    @abc.abstractmethod
    def create_kernel_package(self):
        """
        The main responsibility
        :return: an AbstractModeller and AbstractSolver
        """
