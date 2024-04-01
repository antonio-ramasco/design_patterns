from creational.factory_method import FactoryMethod
import pytest
def test_factory_method_good_case():
    class A:
        pass

    class B:
        def __init__(self, name):
            self._name = name

    factory = FactoryMethod()
    factory.register("A", A)
    factory.register("B", B)
    a =factory.create_instance("A")
    b1 = factory.create_instance("B", "b_object1")
    b2 = factory.create_instance("B", "b_object2")
    assert isinstance(a, A)
    assert isinstance(b1, B)
    assert isinstance(b2, B)
    assert b1._name=="b_object1"
    assert b2._name == "b_object2"

def test_factory_method_exceptions():
    class A:
        pass

    class B:
        def __init__(self, name):
            self._name = name

    factory = FactoryMethod()
    factory.register("A", A)
    factory.register("A", A) #nothing to raise already registered
    with pytest.raises(Exception, match="name_id = A alredy registered as class = A different from class = B"):
        factory.register("A", B)

    a = factory.create_instance("A")
    assert isinstance(a, A)

    with pytest.raises(Exception, match="name_id = C was not registered"):
        factory.create_instance("C")
