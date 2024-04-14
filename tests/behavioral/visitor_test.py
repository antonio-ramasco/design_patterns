from behavioral.visitor import (
    ConcreteElementA,
    ConcreteElementB,
    ConcreteVisitor1,
    ConcreteVisitor2,
    client_code,
)


def test_visitor():
    components = [ConcreteElementA()]

    visitor1 = ConcreteVisitor1()
    assert client_code(components, visitor1) == ["ConcreteVisitor1.operation A"]

    components.append(ConcreteElementB())
    visitor2 = ConcreteVisitor2()
    assert client_code(components, visitor2) == [
        "ConcreteVisitor2.operation A",
        "ConcreteVisitor2.operation B",
    ]
