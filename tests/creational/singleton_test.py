from creational.singleton import Singleton

def test_singleton():
    Singleton._DEBUG = False

    class SampleClass(metaclass=Singleton):
        def __init__(self, value):
            if Singleton._DEBUG :
                print(f"Initializing {type(self).__name__} with value {value}")
            self.value = value

    base1 = SampleClass("A")
    base2 = SampleClass("B")
    assert base1 is base2
    assert id(base1) == id(base2)
# if singleton.Singleton._DEBUG = True then:
# Singleton __call__ SampleClass new instance
# Initializing SampleClass with value A
# Singleton __call__ SampleClass returning instance id 2189117402760
# cls.__instances={<class 'singleton_test.test_singleton.<locals>.SampleClass'>: <singleton_test.test_singleton.<locals>.SampleClass object at 0x000001FDB190AE88>}
# Singleton __call__ SampleClass get existing instance
# Singleton __call__ SampleClass returning instance id 2189117402760
# cls.__instances={<class 'singleton_test.test_singleton.<locals>.SampleClass'>: <singleton_test.test_singleton.<locals>.SampleClass object at 0x000001FDB190AE88>}




