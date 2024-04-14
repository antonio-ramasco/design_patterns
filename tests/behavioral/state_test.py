from behavioral.state import Context, ConcreteStateA, ConcreteStateB

def test_state():
    concrete_state_a=ConcreteStateA()
    context=Context(concrete_state_a)
    assert context.request()==concrete_state_a.handle()

    concrete_state_b=ConcreteStateB()
    context_b=Context(concrete_state_b)
    assert context_b.request()==concrete_state_b.handle()
