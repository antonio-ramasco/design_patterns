from creational.prototype import Prototype

def test_factory_method_good_case():

    class HelperTest(Prototype):
         def __init__(self, a, b):
             self._a = a
             self._b = b

    obj1 = HelperTest("hello", [1]*10)
    obj2 = obj1.clone()
    assert id(obj1) != id(obj2)
    assert obj1._a == obj2._a
    assert obj1._b == obj2._b


