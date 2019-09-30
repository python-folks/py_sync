from abc import ABC
from py_sync.common.decorators import method_alias  

class Synchronizable(ABC):

    serializer = None

    @method_alias
    def synchronize(self):
        raise NotImplementedError()

    @synchronize.for_class
    def _synchronize_class(cls):
        raise NotImplementedError()
