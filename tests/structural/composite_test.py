from structural.composite import Leaf, Composite
def test_composite():
        # This way the client code can support the simple leaf components...
        simple = Leaf()
        simple.operation()
        root = Composite()
        first_level = Composite()
        first_level.add(Leaf())
        first_level.add(Leaf())
        first_level.add(Leaf())
        root.add(Leaf())
        root.add(Leaf())
        root.add(first_level)
        root.add(Leaf())

        assert root.operation()== ['Leaf', 'Leaf', ['Leaf', 'Leaf', 'Leaf'], 'Leaf']