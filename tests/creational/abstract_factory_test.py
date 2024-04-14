from creational.abstract_factory import client_code, ConcreteFactory1, ConcreteFactory2, \
    ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2, \
    AbstractProductA, AbstractProductB


def test_abstract_factory1():
    product1a, product1b=client_code(ConcreteFactory1())
    assert isinstance(product1a, AbstractProductA)
    assert isinstance(product1a, ConcreteProductA1)
    assert isinstance(product1b, AbstractProductB)
    assert isinstance(product1b, ConcreteProductB1)
    assert product1a.function_a() == "ProductA1"
    assert product1b.function_b() == "ProductB1"


def test_abstract_factory2():
    product2a, product2b=client_code(ConcreteFactory2())
    assert isinstance(product2a, AbstractProductA)
    assert isinstance(product2b, AbstractProductB)
    assert isinstance(product2a, ConcreteProductA2)
    assert isinstance(product2b, ConcreteProductB2)
    assert product2a.function_a() == "ProductA2"
    assert product2b.function_b() == "ProductB2"