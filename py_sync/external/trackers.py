import warnings
from abc import ABC

from py_sync.config import config 
from py_sync.warnings import DummyImplementationInUse

class ResourceTrackerBase(ABC):

    def __init__(self, store_discriminator, *args, **kwargs):
        self.store_discriminator = store_discriminator
        self._remote_id = kwargs.get('remote_id', None)
        self._local_id = kwargs.get('local_id', None)

    @property
    def local_id(self):
        if self._local_id is None:
            return self.get_local_id()
        return self._local_id

    def get_local_id(self):
        raise NotImplementedError()

    @property
    def remote_id(self):
        if self._remote_id is None:
            return self.get_remote_id()
        return self._remote_id

    def get_remote_id(self):
        raise NotImplementedError()


class DummyTracker(ResourceTrackerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(DummyImplementationInUse(DummyTracker))

    def get_local_id(self):
        return None
