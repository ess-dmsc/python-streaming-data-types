from collections import namedtuple

import flatbuffers

import streaming_data_types.fbschemas.stringevent_vs00.StringEvent as StringEvent
from streaming_data_types.utils import check_schema_identifier

FILE_IDENTIFIER = b"vs00"

EventData = namedtuple(
    "EventData",
    ("timestamp", "source_name", "data"),
)


def deserialise_vs00(buffer) -> EventData:
    check_schema_identifier(buffer, FILE_IDENTIFIER)
    event = StringEvent.StringEvent.GetRootAs(buffer, 0)

    return EventData(
        event.Timestamp(),
        event.SourceName().decode("utf-8"),
        event.Data().decode("utf-8"),
    )


def serialise_vs00(source_name: str, timestamp: int, value: str) -> bytes:

    builder = flatbuffers.Builder(128)
    builder.ForceDefaults(True)

    source = builder.CreateString(source_name)
    data_str = builder.CreateString(value)

    # Build the actual buffer
    StringEvent.StringEventStart(builder)
    StringEvent.StringEventAddSourceName(builder, source)
    StringEvent.StringEventAddTimestamp(builder, timestamp)
    StringEvent.StringEventAddData(builder, data_str)
    data = StringEvent.StringEventEnd(builder)

    builder.Finish(data, file_identifier=FILE_IDENTIFIER)
    return bytes(builder.Output())
