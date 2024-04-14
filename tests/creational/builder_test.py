from creational.builder import Director, ConcreteBuilderA

def test_builder():
    builderA = ConcreteBuilderA("product_a")
    director = Director(builderA)
    product = director.construct()
    assert str(product) == "product_a;build_part1;build_part2"
