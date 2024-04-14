from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    def __init__(self, state: State) -> None:
        self._state = state

    def request(self):
        self._state.handle()

class State(ABC):
    @abstractmethod
    def handle(self) :
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA handle")

class ConcreteStateB(State):
    def handle(self) -> None:
        print("ConcreteStateB handle")

if __name__ == "__main__":

    context = Context(ConcreteStateA())
    context.request()

    context = Context(ConcreteStateB())
    context.request()
