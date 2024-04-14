from abc import ABC, abstractmethod

class Component(ABC):
    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self) -> None:
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = []
        for g in self._children:
            results.append(g.operation())
        return results

