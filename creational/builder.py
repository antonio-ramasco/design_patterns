from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_part1(self):
        pass

    @abstractmethod
    def build_part2(self):
        pass

class ProductA:
    def __init__(self, name):
        self.__name = name

    def add(self, part):
        self.__name +=";"+part

    def __str__(self):
        return self.__name


class ConcreteBuilderA(Builder):

    def __init__(self, name):
        self.product = ProductA(name)

    def build_part1(self):
        self.product.add("build_part1")

    def build_part2(self):
        self.product.add("build_part2")

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        self.__builder.build_part1()
        self.__builder.build_part2()
        return self.__builder.get_result()
