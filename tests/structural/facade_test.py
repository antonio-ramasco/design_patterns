from structural.facade import Facade, SubSystem1, SubSystem2, SubSystem3
def test_facade():
    facade = Facade()
    facade.add_subsystem(SubSystem1())
    facade.add_subsystem(SubSystem2())
    facade.add_subsystem(SubSystem3())
    assert facade.request() == ['Subsystem1.operation1', 'Subsystem2.operation2', 'Subsystem2.operation2', 'Subsystem3.operation2', 'Subsystem2.operation2']
