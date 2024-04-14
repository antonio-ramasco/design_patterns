from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def function_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def function_a(self) -> str:
        return "ProductA1"

class ConcreteProductA2(AbstractProductA):
    def function_a(self) -> str:
        return "ProductA2"

class AbstractProductB(ABC):
    @abstractmethod
    def function_b(self) -> str:
        pass

class ConcreteProductB1(AbstractProductB):
    def function_b(self) -> str:
        return "ProductB1"

class ConcreteProductB2(AbstractProductB):
    def function_b(self) -> str:
        return "ProductB2"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> tuple(AbstractProductA, AbstractProductB):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    return product_a, product_b
