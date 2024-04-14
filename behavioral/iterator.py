from collections.abc import Iterable, Iterator, MutableSequence

#https://docs.python.org/3/glossary.html#term-iterator

#class collections.abc.Iterator¶
#ABC for classes that provide the __iter__() and __next__() methods. See also the definition of iterator.
#https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator

#class collections.abc.Iterable
#ABC for classes that provide the __iter__() method.
#Checking isinstance(obj, Iterable) detects classes that are registered as Iterable or that have an __iter__() method, but it does not detect classes that iterate with the __getitem__() method. The only reliable way to determine whether an object is iterable is to call iter(obj).
#https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable

#class collections.abc.MutableSequence
#An iterable which supports efficient element access using integer indices via the __getitem__() special method and defines a __len__() method that returns the length of the sequence. Some built-in sequence
#ABCs for read-only and mutable sequences.
#The collections.abc.Sequence abstract base class defines a much richer interface that goes beyond just __getitem__() and __len__(), adding count(), index(), __contains__(), and __reversed__(). Types

class ConcreteIterator(Iterator):

    def __init__(self, array ):
        self._array = array
        self._position = 0

    def __next__(self):
        lenght = len(self._array)
        if self._position>=lenght:
            raise StopIteration()
        value = self._array[self._position]
        self._position += 1
        return value


class ConcreteIterable(MutableSequence):
    #__iter__ from Iterable class
    def __iter__(self):
        return ConcreteIterator(self)

    #another example without iterator
    # def __iter__(self):
    #     for elem in self._data:
    #         yield elem

    def __init__(self) :
        self._data = []

    #MutableSequence Method
    def __getitem__(self, index):
        return self._data[index]

    #MutableSequence Method
    def __len__(self):
        return len(self._data)

    #MutableSequence Method
    def __delitem__(self, index):
        del self._data[index]

    # MutableSequence Method
    def __setitem__(self, index, newvalue):
        self._data[index]=newvalue

    #MutableSequence Method
    def append(self, item) -> None:
        self._data.append(item)

    #MutableSequence Method
    def insert(self, index: int, newvalue):
        self._data[index]=newvalue
