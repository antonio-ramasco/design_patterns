from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component) -> None:
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def __init__(self, component) -> None:
        super(ConcreteDecoratorA, self).__init__(component)

    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def __init__(self, component) -> None:
        super(ConcreteDecoratorB, self).__init__(component)

    def operation(self) -> str:
        return  f"ConcreteDecoratorB({self._component.operation()},{self.added_behaviour()})"

    def added_behaviour(self):
        return "ConcreteDecoratorB_behaviour"
