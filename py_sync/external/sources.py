from abc import ABC

from py_sync.config import config
from .resources import ExternalResource

class ExternalSourceBase(ABC):

    id_register = set()
    serializer = config.DEFAULT_SERIALIZER_CLASS()

    def __init__(self, discriminator, schema=None, source_url=None):
        self.source_url = source_url
        self.schema = schema
        if discriminator in self.id_register:
            raise ValueError(
                f'The id {discriminator} is already in use by other ExternalSource.'
            )
        else:
            self.discriminator = discriminator
            self.id_register.add(discriminator)

    def _bind_ExternalResource(self, obj):
        external_id = self.extract_external_id(obj)
        local_data = self.to_local_data(obj)
        return ExternalResource(external_id, self, local_data)

    def resource_url(self, resource):
        raise NotImplementedError()

    def to_local_data(self, obj):
        local_data = self.serializer.load(obj)
        if self.schema is not None:
            self.schema.validate(local_data)
        return local_data

    def extract_external_id(self, obj):
        raise NotImplementedError()

    def count_external_objects(self):
        raise NotImplementedError()

    def all_external_objects(self):
        raise NotImplementedError()

    def all_external_resources(self):
        return map(self._bind_ExternalResource, self.all_external_objects())

    def __repr__(self):
        return f'<{self.__class__.__name__}/{self.discriminator}/@{self.source_url}>'