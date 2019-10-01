import warnings
from abc import ABC

from py_sync.config import config 
from py_sync.warnings import DummyImplementationInUse

class ResourceTrackerBase(ABC):

    def __init__(self, source, remote_id, *args, **kwargs):
        self.source = source
        self.remote_id = remote_id

    local_id = property(get_local_id)
    def get_local_id(self):
        raise NotImplementedError()


class DummyTracker(ResourceTrackerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(DummyImplementationInUse(DummyTracker))

    def get_local_id(self):
        return None
