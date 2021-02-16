# An iterator pattern allows traversal of a complex data structure easily without exposing the inner workings

# The iterable needs to implement __iter__ and the iterator needs to implement ___next__


#Lets first try and implement https://refactoring.guru/design-patterns/iterator/python/example

from collections.abc import Iterable,Iterator

class AlphabeticalOrderIterator(Iterator):
    _position:int=None #This will store the position of the iterator

    _reverse:bool=False  #This will tell if we want the output in reverse

    def __init__(self,collection:'WordsCollection',reverse:bool=False)->None:
        self._collection=collection
        self._reverse=reverse
        if reverse:
            self._position=-1
        else:
            self._position=0
        
    def __next__(self):
        """
        The method should return the next method in the sequence after finishing it should send stop iteration
        """

        try:
            value=self._collection[self._position]
            if self._reverse:
                self._position+=-1
            else:
                self._reverse+=1
        
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self,collection:'List[Any]'=[])->None:
        self._collection=collection

    def __iter__(self):
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self._collection,True)
    
    def add_item(self,item:'Any'):
        self._collection.append(item)





class different_List():

    def __init__(self,list):
        self._list=list
        self._position=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            value=self._list[self._position]*2
            self._position+=1
        except IndexError:
            raise StopIteration()
        
        return value 

