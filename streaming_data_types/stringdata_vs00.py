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
        [event.Data(i).decode("utf-8") for i in range(event.DataLength())],
    )


def serialise_vs00(
    source_name: str,
    timestamp: int = 0,
    data: list[str] = None,
) -> bytes:
    """
    Serialise string data as a vs00 FlatBuffers message.

    :param source_name:
    :param timestamp:
    :param data:
    :return:
    """
    if data is None:
        data = [""]

    builder = flatbuffers.Builder(1024)
    source = builder.CreateString(source_name)
    string_offsets = [builder.CreateString(s) for s in data]
    vs00Message.vs00_StringDataStartDataVector(
        builder,
        len(string_offsets),
    )
    for offset in reversed(string_offsets):
        builder.PrependUOffsetTRelative(offset)

    data_vector = builder.EndVector()

    vs00Message.vs00_StringDataStart(builder)
    vs00Message.vs00_StringDataAddSourceName(builder, source)
    vs00Message.vs00_StringDataAddTimestamp(builder, timestamp)
    vs00Message.vs00_StringDataAddData(builder, data_vector)

    end = vs00Message.vs00_StringDataEnd(builder)
    builder.Finish(end, file_identifier=FILE_IDENTIFIER)

    return bytes(builder.Output())
