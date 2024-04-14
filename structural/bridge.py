from abc import ABC, abstractmethod
class Abstraction(ABC):
    def __init__(self, implementation) -> None:
        self._impl = implementation

    def operation(self):
        return "Abstraction "+self._impl.operation_impl()

class RefinedAbstraction(Abstraction):
    def __init__(self, implementation) -> None:
        super(RefinedAbstraction, self).__init__(implementation)

    def operation(self):
        return "RefinedAbstraction "+self._impl.operation_impl()

class Implementator(ABC):
    @abstractmethod
    def operation_impl(self):
        pass

class ConcreteImplementatorA(Implementator):
    def operation_impl(self):
        return "ConcreteImplementatorA: operation"

class ConcreteImplementatorB(Implementator):
    def operation_impl(self):
        return "ConcreteImplementatorB: operation"
