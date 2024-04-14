from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        return "ConcreteStateA.handle()"

class ConcreteStateB(State):
    def handle(self):
        return "ConcreteStateB.handle()"

class Context:
    def __init__(self, state):
        self._state=state

    def request(self):
        return self._state.handle()
