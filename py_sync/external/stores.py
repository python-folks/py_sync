from abc import ABC
from rx import Observable, operators

from py_sync.config import config
from .resources import ExternalResource

class StoreBase(ABC):

    id_register = set()
    serializer = config.DEFAULT_SERIALIZER_CLASS()

    def __init__(self, discriminator, schema=None, source_url=None):
        self.source_url = source_url
        self.schema = schema
        if discriminator in self.id_register:
            raise ValueError(
                f'The id {discriminator} is already in use by other Store.'
            )
        else:
            self.discriminator = discriminator
            self.id_register.add(discriminator)

    def _to_ExternalResource(self, obj):
        external_id = self.extract_external_id(obj)
        local_data = self.to_local_data(obj)
        return ExternalResource.from_remote(self, external_id, local_data)

    def resource_url(self, resource):
        raise NotImplementedError()

    def to_local_data(self, obj):
        local_data = self.serializer.load(obj)
        if self.schema is not None:
            self.schema.validate(local_data)
        return local_data

    def to_remote_data(self, obj):
        remote_data = self.serializer.dump(obj)
        return remote_data

    def extract_external_id(self, obj):
        raise NotImplementedError()

    def count_external_objects(self) -> int:
        raise NotImplementedError()

    def external_objects(self) -> Observable:
        raise NotImplementedError()

    def external_resources(self) -> Observable:
        return self.external_objects().pipe(
            operators.map(self._to_ExternalResource)
        )

    def __repr__(self):
        return f'<{self.__class__.__name__}/{self.discriminator}/@{self.source_url}>'