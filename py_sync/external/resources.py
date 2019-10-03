from  py_sync.config import config

from .trackers import ResourceTrackerBase
from .stores import StoreBase

class ExternalResource:

    tracker_class = config.DEFAULT_TRACKER_CLASS
    
    def __init__(self, external_id=None, source=None, local_data=None):
        self.external_id = external_id
        self.data = local_data
        self.source = None
        if isinstance(source, StoreBase):
            self.source = source
        self.tracker = None
        if isinstance(self.tracker_class, ResourceTrackerBase):
            self.tracker = self.tracker_class(source.discriminator, self.external_id)
        
    @property
    def is_tracked(self):
        return self.local_id is not None
        
    @property
    def local_id(self):
        if self.tracker:
            return self.tracker.local_id
        return None

        
