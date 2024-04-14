class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state=state

class Originator:
    def __init__(self):
        self._memento=None

    def set_memento(self, memento):
        self._memento=memento

    def create_memento(self):
        state="my_little_mememnto_state"
        self._memento=Memento(state)
        return self._memento

    @property
    def state(self):
        if self._memento is None:
            return None
        return self._memento.get_state()

class Caretaker():
    def __init__(self):
        originator=Originator()
        self._memento=originator.create_memento()

    @property
    def state(self):
        return self._memento.get_state()