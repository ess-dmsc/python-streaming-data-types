import pytest
from streaming_data_types.nicos_typed_cache_ns11 import serialise_ns11, deserialise_ns11
from streaming_data_types import SERIALISERS, DESERIALISERS


class TestSerialisationNs11:
    def test_serialises_and_deserialises_ns11_message_correctly(self):
        """
        Round-trip to check what we serialise is what we get back.
        """
        original_entry = {
            "key": "some_key",
            "time_stamp": 123456,
            "ttl": 567890,
            "expired": True,
            "value": "some_value",
        }

        buf = serialise_ns11(**original_entry)
        entry = deserialise_ns11(buf)

        assert entry.key == original_entry["key"]
        assert entry.time_stamp == original_entry["time_stamp"]
        assert entry.ttl == original_entry["ttl"]
        assert entry.expired == original_entry["expired"]
        assert entry.value == original_entry["value"]

    def test_if_buffer_has_wrong_id_then_throws(self):
        original_entry = {
            "key": "some_key",
            "time_stamp": 123456,
            "ttl": 567890,
            "expired": True,
            "value": "some_value",
        }
        buf = serialise_ns11(**original_entry)

        # Manually hack the id
        buf = bytearray(buf)
        buf[4:8] = b"1234"

        with pytest.raises(RuntimeError):
            deserialise_ns11(buf)

    def test_schema_type_is_in_global_serialisers_list(self):
        assert "ns11" in SERIALISERS
        assert "ns11" in DESERIALISERS