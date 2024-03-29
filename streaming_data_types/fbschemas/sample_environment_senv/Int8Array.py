# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Int8Array(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsInt8Array(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Int8Array()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def Int8ArrayBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x73\x65\x6E\x76", size_prefixed=size_prefixed
        )

    # Int8Array
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Int8Array
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int8Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1),
            )
        return 0

    # Int8Array
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # Int8Array
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Int8Array
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def Int8ArrayStart(builder):
    builder.StartObject(1)


def Int8ArrayAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0
    )


def Int8ArrayStartValueVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)


def Int8ArrayEnd(builder):
    return builder.EndObject()
