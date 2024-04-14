from structural.decorator import (
    ConcreteComponent,
    ConcreteDecoratorA,
    ConcreteDecoratorB,
)


def test_decorator():

    simple = ConcreteComponent()
    assert simple.operation() == "ConcreteComponent"
    decorator_a = ConcreteDecoratorA(simple)
    assert decorator_a.operation() == "ConcreteDecoratorA(ConcreteComponent)"
    decorator_b_a = ConcreteDecoratorB(decorator_a)
    assert (
        decorator_b_a.operation()
        == "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent),ConcreteDecoratorB_behaviour)"
    )
    decorator_a_b_a = ConcreteDecoratorA(decorator_b_a)
    assert (
        decorator_a_b_a.operation()
        == "ConcreteDecoratorA(ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent),ConcreteDecoratorB_behaviour))"
    )
    decorator_b_b_a = ConcreteDecoratorB(decorator_b_a)
    assert (
        decorator_b_b_a.operation()
        == "ConcreteDecoratorB(ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent),ConcreteDecoratorB_behaviour),ConcreteDecoratorB_behaviour)"
    )
