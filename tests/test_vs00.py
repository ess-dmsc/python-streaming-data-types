import numpy as np
import pytest

from streaming_data_types import DESERIALISERS, SERIALISERS
from streaming_data_types.stringdata_vs00 import deserialise_vs00, serialise_vs00
from streaming_data_types.exceptions import WrongSchemaException


class TestSerialisationVs00:
    def test_serialises_and_deserialises_message_correctly(self):
        """
        Round-trip to check what we serialise is what we get back.
        """
        original_entry = {
            "source_name": "some_source",
            "timestamp": 123456789,
            "data": "hello",
        }

        buf = serialise_vs00(**original_entry)
        entry = deserialise_vs00(buf)

        assert entry.source_name == original_entry["source_name"]
        assert entry.timestamp == original_entry["timestamp"]
        assert entry.data == original_entry["data"]

    def test_if_buffer_has_wrong_id_then_throws(self):
        original_entry = {
            "source_name": "some_source",
            "timestamp": 123456789,
            "data": "hello",
        }

        buf = serialise_vs00(**original_entry)
        entry = deserialise_vs00(buf)

        # Manually introduce error in id.
        buf = bytearray(buf)
        buf[4:8] = b"1234"

        with pytest.raises(WrongSchemaException):
            deserialise_vs00(buf)

    def test_schema_type_is_in_global_serialisers_list(self):
        assert "vs00" in SERIALISERS
        assert "vs00" in DESERIALISERS
