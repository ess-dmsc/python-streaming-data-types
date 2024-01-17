# automatically generated by the FlatBuffers compiler, do not modify

# namespace:


import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class ArrayInt64(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArrayInt64()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsArrayInt64(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def ArrayInt64BufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x68\x73\x30\x32", size_prefixed=size_prefixed
        )

    # ArrayInt64
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayInt64
    def Value(self, j: int):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # ArrayInt64
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArrayInt64
    def ValueLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArrayInt64
    def ValueIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def ArrayInt64Start(builder: flatbuffers.Builder):
    builder.StartObject(1)


def Start(builder: flatbuffers.Builder):
    ArrayInt64Start(builder)


def ArrayInt64AddValue(builder: flatbuffers.Builder, value: int):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0
    )


def AddValue(builder: flatbuffers.Builder, value: int):
    ArrayInt64AddValue(builder, value)


def ArrayInt64StartValueVector(builder, numElems: int) -> int:
    return builder.StartVector(8, numElems, 8)


def StartValueVector(builder, numElems: int) -> int:
    return ArrayInt64StartValueVector(builder, numElems)


def ArrayInt64End(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()


def End(builder: flatbuffers.Builder) -> int:
    return ArrayInt64End(builder)
