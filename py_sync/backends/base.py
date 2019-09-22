from abc import ABC
from functools import singledispatch 

class Synchronizable(ABC):
    
    @singledispatch
    def synchronize(*args, **kwargs):
        pass

    @synchronize.register(object)
    def _synchronize_instance(self):
        print("Called for instance")

    @synchronize.register(type(None))
    def _synchronize_class():
        print("Called for class")

