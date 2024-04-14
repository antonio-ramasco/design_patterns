from behavioral.observer import ConcreteSubject, ConcreteObserver
def test_observer():
    subject = ConcreteSubject("subject1")
    subject.set_state("hello")
    observer_a = ConcreteObserver("A")

    subject.attach(observer_a)
    assert subject.notify()==['updated observer A with message subject1:hello']

    subject.set_state("everybody")
    assert subject.notify()==['updated observer A with message subject1:everybody']

    observer_a = ConcreteObserver("B")
    subject.attach(observer_a)
    subject.set_state("hello again")

    assert subject.notify()==['updated observer A with message subject1:hello again', 'updated observer B with message subject1:hello again']

