class Facade:

    def __init__(self):
        self._subystems=[]

    def add_subsystem(self, subsystem):
        self._subystems.append(subsystem)

    def request(self) -> str:
        operations = []
        for subsystem in self._subystems:
            #only facade knows all the sub systems
            operations.append(subsystem.operation1())
            if isinstance(subsystem, SubSystem2):
                operations.append(subsystem.operation2())
            if isinstance(subsystem, SubSystem3):
                operations.append(subsystem.operation3())
        return operations

class SubSystem1:
    def operation1(self):
        return "Subsystem1.operation1"

class SubSystem2:
    def operation1(self):
        return "Subsystem2.operation2"

    def operation2(self):
        return "Subsystem2.operation2"

class SubSystem3:
    def operation1(self):
        return "Subsystem3.operation2"
    def operation3(self):
        return "Subsystem2.operation2"
