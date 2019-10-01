import warnings
from abc import ABC

from py_sync.warnings import DummyImplementationInUse

class SerializerBase(ABC):

    def __init__(self, *args, **kwargs):
        pass 

    def load(self, obj):
        raise NotImplementedError()

class DummySerializer(SerializerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(DummyImplementationInUse(DummySerializer))

    def load(self, obj):
        return obj