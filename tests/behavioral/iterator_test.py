from behavioral.iterator import ConcreteIterable
def test_iterator():
    array = ConcreteIterable()
    assert len(array)==0
    item1 = "item1"
    item2 = "item2"

    array.append(item1)
    array.append(item2)
    assert len(array) == 2
    #test iteration works
    for item in array:
        print(item)

