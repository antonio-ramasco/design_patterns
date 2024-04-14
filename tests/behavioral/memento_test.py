from behavioral.memento import Memento, Caretaker, Originator


def test_memento():
    m = Memento("XXX1")
    assert m.get_state() == "XXX1"
    m.set_state("XXX")
    assert m.get_state() == "XXX"


def test_originator():
    originator = Originator()
    assert originator.state is None

    memento = originator.create_memento()
    assert memento.get_state() == originator.state

    memento1 = Memento("XXX")
    originator.set_memento(memento1)
    assert memento1.get_state() == originator.state


def test_caretaker():
    care_taker = Caretaker()
    care_taker.state == Originator().create_memento().get_state()
