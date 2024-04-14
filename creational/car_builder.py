from abc import ABC, abstractmethod

class Body:
    def __init__(self, shape_name):
        self.__shape = shape_name
    def __str__(self):
        return self.__shape

class Car:
    def __init__(self):
        self.__body = None
        self.__brand = None

    def set_body(self, body, brand):
        self.__body = body
        self.__brand = brand

    def __str__(self):
        return f"brand; {self.__brand}, body: {self.__body}"

class CarBuilder(ABC):
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


class JeepLayoutBuilder(CarBuilder):

    def __init__(self):
        self.__car=Car()

    def build_body(self,brand):
        self.__car.set_body("SUV1X", brand)

    def get_car(self):
        return self.__car


class HondaDirector:
    def __init__(self):
        pass

    def create_car(self, builder):
        self.__builder=builder
        self.__builder.build_body(brand="Honda")
