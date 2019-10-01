from .common.utils import attrdict
from .external.trackers import NoneTracker
from .external.serializers import DummySerializer

config = attrdict(
    DEFAULT_TRACKER_CLASS=NoneTracker,
    DEFAULT_SERIALIZER_CLASS=DummySerializer,
)