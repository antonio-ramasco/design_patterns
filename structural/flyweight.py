from abc import ABC, abstractmethod
class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinstic_state):
        pass

class ConcreteFlyweight(Flyweight):
    def __init__(self, intrisic_state):
        self._initrisic_state=intrisic_state

    def operation(self, extrinstic_state):
        return f"op extrinstic_state={extrinstic_state} with initrisic_state={self._initrisic_state}"

class UnsharedConcreteFlyweight(Flyweight):
    def __init__(self, all_state):
        self._all_state = all_state

    def operation(self, extrinstic_state):
        return f"op extrinstic_state={extrinstic_state} with all_state={self._all_state}"

class FlyweightFactory():
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key, *args, **kwargs):
        if key in self._flyweights:
            return self._flyweights
        else:
            if key==UnsharedConcreteFlyweight.__name__:
                new_flyweight=UnsharedConcreteFlyweight(*args, **kwargs)
            elif key==ConcreteFlyweight.__name__:
                new_flyweight = ConcreteFlyweight(*args, **kwargs)
            else:
                raise KeyError(f"key {key} not supported for a FlyweightFactory supported[{UnsharedConcreteFlyweight.__name__}, {ConcreteFlyweight.__name__}] ")
            self._flyweights[key]=new_flyweight
            return new_flyweight