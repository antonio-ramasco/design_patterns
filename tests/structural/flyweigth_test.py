from structural.flyweight import FlyweightFactory, ConcreteFlyweight, UnsharedConcreteFlyweight
import pytest

def test_flyweigth_key_error():
    factory=FlyweightFactory()
    with pytest.raises(KeyError) as exc_info:
        factory.get_flyweight("wrong_keyXXX","")

    assert "wrong_keyXXX not supported for a FlyweightFactory supported[UnsharedConcreteFlyweight, ConcreteFlyweight]" in str(exc_info.value)

def test_flyweigth_concrete_flyweight():
    factory=FlyweightFactory()
    flyweight=factory.get_flyweight("ConcreteFlyweight","XXX")
    assert flyweight.operation("YYY")=="op extrinstic_state=YYY with initrisic_state=XXX"

def test_flyweigth_unshared_concrete_flyweight():
    factory=FlyweightFactory()
    flyweight=factory.get_flyweight("UnsharedConcreteFlyweight","XXX")
    assert flyweight.operation("YYY")=="op extrinstic_state=YYY with all_state=XXX"
