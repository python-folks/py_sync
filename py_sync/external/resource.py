


class ExternalResource:

    tracker_class = None
    
    def __init__(self, source=None, external_data=None):
        self.data = external_data
        self.source = source

    @property
    def is_tracked(self):
        return False