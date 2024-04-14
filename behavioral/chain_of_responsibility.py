from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle_request(self):
        pass

    def __init__(self):
        self._successor = None

    def set_successor(self, handler):
        self._successor=handler
        return self

    @property
    def successor(self):
        return self._successor

class ConcreteHandler1(Handler):
    def handle_request(self):
        if self._successor is not None:
            return self._successor.handle_request()
        return None

class ConcreteHandler2(Handler):
    def handle_request(self):
        if self._successor is not None:
            return self._successor.handle_request()
        return None

class ConcreteHandler3(Handler):
    def handle_request(self):
        return "ConcreteHandler3.request_handled"

