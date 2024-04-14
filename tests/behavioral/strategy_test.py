from behavioral.strategy import Context, ConcreteStrategyA, ConcreteStrategyB
def test_strategy():
    strategy_a=ConcreteStrategyA()
    context=Context(strategy_a)
    assert context.context_interface()==strategy_a.algorithm_interface()

    strategy_b=ConcreteStrategyB()
    context_b=Context(strategy_b)
    assert context_b.context_interface()==strategy_b.algorithm_interface()