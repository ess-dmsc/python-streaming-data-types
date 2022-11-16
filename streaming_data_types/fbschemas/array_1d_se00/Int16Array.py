# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Int16Array(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Int16Array()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsInt16Array(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def Int16ArrayBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x73\x65\x30\x30", size_prefixed=size_prefixed
        )

    # Int16Array
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Int16Array
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int16Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2),
            )
        return 0

    # Int16Array
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int16Flags, o)
        return 0

    # Int16Array
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Int16Array
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def Int16ArrayStart(builder):
    builder.StartObject(1)


def Start(builder):
    return Int16ArrayStart(builder)


def Int16ArrayAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0
    )


def AddValue(builder, value):
    return Int16ArrayAddValue(builder, value)


def Int16ArrayStartValueVector(builder, numElems):
    return builder.StartVector(2, numElems, 2)


def StartValueVector(builder, numElems):
    return Int16ArrayStartValueVector(builder, numElems)


def Int16ArrayEnd(builder):
    return builder.EndObject()


def End(builder):
    return Int16ArrayEnd(builder)