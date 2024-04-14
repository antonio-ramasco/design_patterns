from behavioral.mediator import Mediator, ConcreteColleague1, ConcreteColleague2, ConcreteMediator
def test_mediator():
    mediator= ConcreteMediator()
    colleague1=ConcreteColleague1(mediator)
    colleague2 = ConcreteColleague2(mediator)
    colleague1.send("HELLO")
    assert colleague2.pop_last_message()=="ConcreteColleague2 received message: HELLO"
    assert colleague1.pop_last_message()=="ConcreteColleague1 received message: HELLO"
    assert colleague2.pop_last_message() is None
    assert colleague1.pop_last_message() is None