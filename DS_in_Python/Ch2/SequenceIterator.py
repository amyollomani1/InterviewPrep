class SequenceIterator:
    #An iterator for any of Python's sequence types
    
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1
        
    def __next__(self):
        #reutrns next element
        self._k +=1 #advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k]) #return the data element
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self #by convenction, iterator must return itself as an iterator
    
    
        