from abc import ABC, abstractmethod

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def __init__(self, value):
        self._value=value

    def interpret(self, context):
        return self._value

class NonTerminalExpression(AbstractExpression):
    def __init__(self, expressions):
        self._expressions =[]
        for expr in expressions:
           self._expressions.append(expr)

    def interpret(self, context):
        res=[]
        for expression in self._expressions:
            res.append(expression.interpret(context))
        if context.get_state().upper()=="SUM":
            return sum(res)
        return None

class Context:
    def __init__(self, state):
        self._state=state

    def get_state(self):
        return self._state
