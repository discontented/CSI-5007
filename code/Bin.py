import numpy as np

class Bin():
    
    def __init__(self, weight, contents=[]):
        """Initializes a bin at max capacity of weight with contents.
        
        Arguments:
            weight {int} -- Max capacity of bin.
        
        Keyword Arguments:
            contents {list} -- Contents of bin. (default: {[]})
        """
        self.weight = weight
        if(type(contents) is not list):
            self.contents = [contents] 
        else:
            self.contents = contents
            
    def capacity(self):
        """Returns capacity left in bin.
        """
        return self.weight - np.sum(self.contents)
    
    def insert(self, item):
        """Inserts an item into bin if there is room for it.
        
        Arguments:
            item {int} -- An item with its value being its weight or size.
        """
        if(item <= self.capacity()):
            self.contents.append(item)
        else:
            raise ValueError("Item doesn't fit")
