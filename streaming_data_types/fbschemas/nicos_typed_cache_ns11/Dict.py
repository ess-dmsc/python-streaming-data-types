# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()


class Dict(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDict(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Dict()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DictBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset,
                                                    b"\x6E\x73\x31\x31",
                                                    size_prefixed=size_prefixed)

    # Dict
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Dict
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from DictMapping import DictMapping
            obj = DictMapping()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Dict
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Dict
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def DictStart(builder):
    builder.StartObject(1)


def DictAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.
                                        UOffsetTFlags.py_type(value), 0)


def DictStartValueVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def DictEnd(builder):
    return builder.EndObject()