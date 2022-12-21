from ctypes import *

class Array1D:
    def __init__(self, size):
        a = py_object*size #ji zhu jiu xing le
        self._elements = a()
        self.clear(None)
    
    def __len__(self):
        return len(self._elements)

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __getitem__(self, index):
        return self._elements[index]
    
    def __setitem__(self, index, value):
        self._elements[index] = value


