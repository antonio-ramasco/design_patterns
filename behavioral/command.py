from abc import ABC, abstractmethod
class Reicever():
    def action(self):
        return "reicever.action"

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def __init__(self, receiver):
        self._receiver=receiver

class ConcreteCommand(Command):
    def execute(self):
        return "ConcreteCommand."+self._receiver.action()

class Invoker:
    def __init__(self):
        self._command=None

    def store_command(self, command):
        self._command=command

    def execute(self):
        if self._command is None:
            return None
        return self._command.execute()