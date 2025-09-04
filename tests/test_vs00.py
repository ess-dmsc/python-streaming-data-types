import pytest

from streaming_data_types.stringevent_vs00 import deserialise_vs00, serialise_vs00


class TestSerialisationVS00:
    def test_vs00_serialization_deserialization(self):
        # Example data for vs00
        source_name = "test_source"
        value = "All happy?"
        timestamp = 1625077800

        # Serialize
        serialized = serialise_vs00(source_name, timestamp, value)
        assert isinstance(serialized, bytes)

        # Deserialize
        deserialized = deserialise_vs00(serialized)
        assert deserialized.source_name == source_name
        assert deserialized.data == value
        assert deserialized.timestamp == timestamp

    def test_vs00_invalid_value_serialization(self):
        # Test with invalid types
        with pytest.raises(TypeError):
            serialise_vs00("source_123", 23, 123.4)

    def test_vs00_invalid_timestamp_serialization(self):
        # Test with invalid types
        with pytest.raises(TypeError):
            serialise_vs00("source_123", "23", "a failure")

    def test_vs00_invalid_source_serialization(self):
        # Test with invalid types
        with pytest.raises(TypeError):
            serialise_vs00(13, 23, "another failure")

    def test_vs00_long_string(self):
        # Test with edge float values
        source_name = "long_test"
        value = "a" * 70000  # Very long string
        timestamp = 1625077800
        serialized = serialise_vs00(source_name, timestamp, value)
        deserialized = deserialise_vs00(serialized)
        assert deserialized.source_name == source_name
        assert deserialized.data == value
        assert deserialized.timestamp == timestamp

    def test_vs00_empty_string(self):
        # Test with edge float values
        source_name = "empty_test"
        value = ""  # Empty string
        timestamp = 1625077800
        serialized = serialise_vs00(source_name, timestamp, value)
        deserialized = deserialise_vs00(serialized)
        assert deserialized.source_name == source_name
        assert deserialized.data == value
        assert deserialized.timestamp == timestamp
