# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Event44Message(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Event44Message()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def Event44MessageBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x65\x76\x34\x34", size_prefixed=size_prefixed
        )

    # Event44Message
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Event44Message
    def SourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Event44Message
    def ReferenceTime(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # Event44Message
    def ReferenceTimeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Event44Message
    def ReferenceTimeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Event44Message
    def ReferenceTimeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Event44Message
    def ReferenceTimeIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # Event44Message
    def ReferenceTimeIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Event44Message
    def ReferenceTimeIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Event44Message
    def ReferenceTimeIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Event44Message
    def TimeOfFlight(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # Event44Message
    def TimeOfFlightAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Event44Message
    def TimeOfFlightLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Event44Message
    def TimeOfFlightIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Event44Message
    def PixelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # Event44Message
    def PixelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Event44Message
    def PixelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Event44Message
    def PixelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0


def Event44MessageStart(builder):
    builder.StartObject(5)


def Start(builder):
    return Event44MessageStart(builder)


def Event44MessageAddSourceName(builder, sourceName):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(sourceName), 0
    )


def AddSourceName(builder, sourceName):
    return Event44MessageAddSourceName(builder, sourceName)


def Event44MessageAddReferenceTime(builder, referenceTime):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(referenceTime), 0
    )


def AddReferenceTime(builder, referenceTime):
    return Event44MessageAddReferenceTime(builder, referenceTime)


def Event44MessageStartReferenceTimeVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def StartReferenceTimeVector(builder, numElems):
    return Event44MessageStartReferenceTimeVector(builder, numElems)


def Event44MessageAddReferenceTimeIndex(builder, referenceTimeIndex):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(referenceTimeIndex), 0
    )


def AddReferenceTimeIndex(builder, referenceTimeIndex):
    return Event44MessageAddReferenceTimeIndex(builder, referenceTimeIndex)


def Event44MessageStartReferenceTimeIndexVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def StartReferenceTimeIndexVector(builder, numElems):
    return Event44MessageStartReferenceTimeIndexVector(builder, numElems)


def Event44MessageAddTimeOfFlight(builder, timeOfFlight):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(timeOfFlight), 0
    )


def AddTimeOfFlight(builder, timeOfFlight):
    return Event44MessageAddTimeOfFlight(builder, timeOfFlight)


def Event44MessageStartTimeOfFlightVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def StartTimeOfFlightVector(builder, numElems):
    return Event44MessageStartTimeOfFlightVector(builder, numElems)


def Event44MessageAddPixelId(builder, pixelId):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(pixelId), 0
    )


def AddPixelId(builder, pixelId):
    return Event44MessageAddPixelId(builder, pixelId)


def Event44MessageStartPixelIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def StartPixelIdVector(builder, numElems):
    return Event44MessageStartPixelIdVector(builder, numElems)


def Event44MessageEnd(builder):
    return builder.EndObject()


def End(builder):
    return Event44MessageEnd(builder)
