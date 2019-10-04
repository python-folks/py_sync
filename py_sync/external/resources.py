from  py_sync.config import config

from .trackers import ResourceTrackerBase
from .stores import StoreBase

class ExternalResource:

    tracker_class = config.DEFAULT_TRACKER_CLASS
    
    def __init__(self, store, data=None, **kwargs):
        self.data = data
        self.tracker = None
        if not isinstance(store, StoreBase):
            raise TypeError("`store` must be an StoreBase instance.")
        self.store = store
        
    @property
    def is_binded(self):
        return self.tracker is not None
        
    def bind_local(self, local_id):
        self.tracker = self.tracker_class(self.store.discriminator, local_id=local_id)
        return self

    @classmethod
    def from_local(cls, store, local_id, data=None):
        instance = cls(store, data)
        return instance.bind_local(local_id)

    def bind_remote(self, remote_id):
        self.tracker = self.tracker_class(self.store.discriminator, external_id=remote_id)
        return self

    @classmethod
    def from_remote(cls, store, remote_id, data=None):
        instance = cls(store, data)
        return instance.bind_remote(remote_id)

    @property
    def is_tracked(self):
        return self.local_id is not None
        
    @property
    def local_id(self):
        if self.tracker:
            return self.tracker.local_id
        return None

    @property
    def remote_id(self):
        if self.tracker:
            return self.tracker.remote_id
        return None

        
