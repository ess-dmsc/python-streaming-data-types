from collections import namedtuple

import flatbuffers

import streaming_data_types.fbschemas.stringdata_vs00.stringdata_vs00 as vs00Message
from streaming_data_types.utils import check_schema_identifier

FILE_IDENTIFIER = b"vs00"


StringData = namedtuple(
    "StringData",
    ("source_name", "timestamp", "data"),
)


def deserialise_vs00(buffer):
    """
    Deserialise FlatBuffer vs00.

    :param buffer: The FlatBuffers buffer.
    :return: The deserialised data.
    """
    check_schema_identifier(buffer, FILE_IDENTIFIER)

    event = vs00Message.vs00_StringData.GetRootAs(buffer, 0)

    return StringData(
        event.SourceName().decode("utf-8"),
        event.Timestamp(),
        event.Data().decode("utf-8"),
    )


def serialise_vs00(
    source_name: str,
    timestamp: int,
    data: str,
) -> bytes:
    """
    Serialise string data as a vs00 FlatBuffers message.

    :param source_name:
    :param timestamp:
    :param data:
    :return:
    """
    builder = flatbuffers.Builder(1024)
    source = builder.CreateString(source_name)
    data_offset = builder.CreateString(data)

    vs00Message.vs00_StringDataStart(builder)
    vs00Message.vs00_StringDataAddSourceName(builder, source)
    vs00Message.vs00_StringDataAddTimestamp(builder, timestamp)
    vs00Message.vs00_StringDataAddData(builder, data_offset)

    end = vs00Message.vs00_StringDataEnd(builder)
    builder.Finish(end, file_identifier=FILE_IDENTIFIER)

    return bytes(builder.Output())
