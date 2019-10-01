
class DummyImplementationInUse(Warning):

    def __init__(self, dummy_class):
        self.dummy_class = dummy_class

    def __str__(self):
        return f'Be aware you are using {self.dummy_class} in your code.'
