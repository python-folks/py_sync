from abc import ABC


class ResourceTrackerBase(ABC):

    def __init__(self, source, remote_id):
        self.source = source
        self.remote_id = remote_id

    local_id = property(get_local_id)
    def get_local_id(self):
        raise NotImplementedError()

    @property
    def is_tracked(self):
        return self.local_id is not None
