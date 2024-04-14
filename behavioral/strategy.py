from abc import ABC, abstractmethod
class Strategy:
    @abstractmethod
    def algorithm_interface(self):
        pass

class ConcreteStrategyA:
    def algorithm_interface(self):
        return "ConcreteStrategyA algo"

class ConcreteStrategyB:
    def algorithm_interface(self):
        return "ConcreteStrategyB algo"

class Context:
    def __init__(self, strategy):
        self._strategy=strategy

    def context_interface(self):
        return self._strategy.algorithm_interface()
