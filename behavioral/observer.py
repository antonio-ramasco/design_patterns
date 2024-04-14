from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        results=[]
        for observer in self._observers:
            observer.update(self)
            results.append(observer.observer_state)
        return results

class ConcreteSubject(Subject):
    def __init__(self, subject_name):
        super(ConcreteSubject, self).__init__()
        self._state = None
        self._subject_name=subject_name

    def get_state(self):
        return self._subject_name+":"+self._state

    def set_state(self, state):
        self._state=state


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name=name
        self._observer_state=None

    def update(self, subject):
        self._observer_state=f"updated observer {self._name} with message {subject.get_state()}"

    @property
    def observer_state(self):
        return self._observer_state
