from behavioral.template_method import ConcreteClassA


def test_template_method():
    a = ConcreteClassA()
    a.template_method()
    assert str(a) == ";primitive_operation_1;primitive_operation_2"
