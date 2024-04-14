from structural.bridge import (
    Abstraction,
    RefinedAbstraction,
    ConcreteImplementatorA,
    ConcreteImplementatorB,
)


def test_bridge():

    implementation = ConcreteImplementatorA()
    abstraction = Abstraction(implementation)
    assert abstraction.operation() == "Abstraction ConcreteImplementatorA: operation"

    implementation = ConcreteImplementatorB()
    abstraction = Abstraction(implementation)
    assert abstraction.operation() == "Abstraction ConcreteImplementatorB: operation"

    implementation = ConcreteImplementatorA()
    abstraction = RefinedAbstraction(implementation)
    assert (
        abstraction.operation()
        == "RefinedAbstraction ConcreteImplementatorA: operation"
    )

    implementation = ConcreteImplementatorB()
    abstraction = RefinedAbstraction(implementation)
    assert (
        abstraction.operation()
        == "RefinedAbstraction ConcreteImplementatorB: operation"
    )
