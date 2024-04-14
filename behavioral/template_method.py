from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def primitive_operation_1(self):
        pass

    @abstractmethod
    def primitive_operation_2(self):
        pass


class AbstractClassWithTemplateMethod(ABC):
    def template_method(self):
        self.primitive_operation_1()
        self.primitive_operation_2()

class ConcreteClassA(AbstractClassWithTemplateMethod):
    def __init__(self):
        self.__internal_str = ""

    def primitive_operation_1(self):
        self.__internal_str+=";primitive_operation_1"

    def primitive_operation_2(self):
        self.__internal_str+=";primitive_operation_2"

    def __str__(self):
        return self.__internal_str