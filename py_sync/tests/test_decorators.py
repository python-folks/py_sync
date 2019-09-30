from unittest import TestCase


from py_sync.common.decorators import method_alias

class TestMethodAlias(TestCase):
    
    def test_zero(self):
        self.assertFalse(False)
