from creational import singleton

def test_singleton():
    class SampleClass(metaclass=singleton.Singleton):
        def __init__(self, value):
            print(f"Initializing {type(self).__name__} with value {value}")
            self.value = value

    singleton.Singleton._DEBUG = False
    base1 = SampleClass("A")
    base2 = SampleClass("B")
    assert base1 is base2
    assert id(base1) == id(base2)
# if singleton.Singleton._DEBUG = True then:
# Initializing SampleClass with value A
# Singleton __call__ SampleClass returning instance id 2402236562056
# cls.__instances={<class 'singleton_test.test_singleton.SampleClass'>:
#     <singleton_test.test_singleton.<locals>.SampleClass object>}
# Singleton __call__ SampleClass get existing instance
# Singleton __call__ SampleClass returning instance id 2402236562056
# cls.__instances={<class 'singleton_test.test_singleton.SampleClass'>:
# <singleton_test.test_singleton.<locals>.SampleClass object>}
