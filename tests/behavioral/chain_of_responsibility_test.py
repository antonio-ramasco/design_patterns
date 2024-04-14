from behavioral.chain_of_responsibility import ConcreteHandler1, ConcreteHandler2, ConcreteHandler3

def test_chain_of_responsability():
    handler1=ConcreteHandler1()
    assert handler1.handle_request() is None
    handler1.set_successor(ConcreteHandler2().set_successor(ConcreteHandler3()))
    assert handler1.handle_request()=="ConcreteHandler3.request_handled"
