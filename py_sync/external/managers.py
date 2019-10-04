from .stores import StoreBase

class StoresManager:

    def __init__(self, stores, schema=None, *args, **kwargs):
        if not isinstance(stores, (list, tuple)):
            raise TypeError("`stores` must be tuple of StoreBases.")
        self.stores = set(stores)
        self.apply_schema(schema)
    

    def apply_schema(self, schema):
        self.schema = schema
        for store in self.stores:
            store.schema = schema

    def refs(self, local_id):
        pass

