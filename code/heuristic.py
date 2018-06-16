import numpy as np

class Bin():
    def __init__(self, weight, contents=[]):
        self.weight = weight
        if(np.sum(contents) <= weight):
            self.contents = contents
        else:
            raise ValueError("Contents are larger than max capacity.")
            
    def capacity(self):
        return self.weight - np.sum(self.contents)
    
    def insert(self, item):
        if(item <= self.capacity()):
            self.contents.append(item)
        else:
            raise ValueError("Item doesn't fit")