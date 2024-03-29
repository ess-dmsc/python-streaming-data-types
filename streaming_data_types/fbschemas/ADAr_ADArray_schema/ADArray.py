# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class ADArray(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsADArray(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ADArray()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def ADArrayBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x41\x44\x41\x72", size_prefixed=size_prefixed
        )

    # ADArray
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ADArray
    def SourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ADArray
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ADArray
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags, o + self._tab.Pos
            )
        return 0

    # ADArray
    def Dimensions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # ADArray
    def DimensionsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # ADArray
    def DimensionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ADArray
    def DimensionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ADArray
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # ADArray
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint8Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1),
            )
        return 0

    # ADArray
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # ADArray
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ADArray
    def DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # ADArray
    def Attributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Attribute import Attribute

            obj = Attribute()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ADArray
    def AttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ADArray
    def AttributesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


def ADArrayStart(builder):
    builder.StartObject(7)


def ADArrayAddSourceName(builder, sourceName):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(sourceName), 0
    )


def ADArrayAddId(builder, id):
    builder.PrependInt32Slot(1, id, 0)


def ADArrayAddTimestamp(builder, timestamp):
    builder.PrependUint64Slot(2, timestamp, 0)


def ADArrayAddDimensions(builder, dimensions):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(dimensions), 0
    )


def ADArrayStartDimensionsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def ADArrayAddDataType(builder, dataType):
    builder.PrependInt8Slot(4, dataType, 0)


def ADArrayAddData(builder, data):
    builder.PrependUOffsetTRelativeSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0
    )


def ADArrayStartDataVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)


def ADArrayAddAttributes(builder, attributes):
    builder.PrependUOffsetTRelativeSlot(
        6, flatbuffers.number_types.UOffsetTFlags.py_type(attributes), 0
    )


def ADArrayStartAttributesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def ADArrayEnd(builder):
    return builder.EndObject()
