from abc import ABC, abstractmethod

class Colleague(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

    @abstractmethod
    def pop_last_message(self):
        pass

class ConcreteColleague1(Colleague):
    def __init__(self, mediator):
        self._mediator = mediator
        self._mediator.add_colleague(self)
        self._last_message = None
    def send(self, message):
        self._mediator.send(message)

    def receive(self, message):
        self._last_message=f"ConcreteColleague1 received message: {message}"

    def pop_last_message(self):
        message=self._last_message
        self._last_message=None
        return message


class ConcreteColleague2(Colleague):
    def __init__(self, mediator):
        self._mediator = mediator
        self._mediator.add_colleague(self)
        self._last_message = None
    def send(self, message):
        self._mediator.send(message)

    def receive(self, message):
        self._last_message=f"ConcreteColleague2 received message: {message}"

    def pop_last_message(self):
        message=self._last_message
        self._last_message=None
        return message




class Mediator(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def add_colleague(self, colleague):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague = []

    def add_colleague(self, colleague):
        self._colleague.append(colleague)

    def send(self, message):
        for colleague in self._colleague:
            colleague.receive(message)