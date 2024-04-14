from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def accept(self, visitor) -> None:
        pass


class ConcreteElementA(Element):
    def accept(self, visitor):
        return visitor.visit_concrete_component_a(self)

    def operation_a(self):
        return "operation A"


class ConcreteElementB(Element):
    def accept(self, visitor):
        return visitor.visit_concrete_component_b(self)

    def operation_b(self):
        return "operation B"



class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        return f"ConcreteVisitor1.{element.operation_a()}"

    def visit_concrete_component_b(self, element) -> None:
        return f"ConcreteVisitor1.{element.operation_b()}"


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        return f"ConcreteVisitor2.{element.operation_a()}"

    def visit_concrete_component_b(self, element) -> None:
        return f"ConcreteVisitor2.{element.operation_b()}"


def client_code(components, visitor):
    results=[]
    for component in components:
        results.append(component.accept(visitor))
    return results

