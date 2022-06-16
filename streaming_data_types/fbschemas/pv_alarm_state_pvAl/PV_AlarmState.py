# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PV_AlarmState(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PV_AlarmState()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPV_AlarmState(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def PV_AlarmStateBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x70\x76\x41\x6C", size_prefixed=size_prefixed)

    # PV_AlarmState
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PV_AlarmState
    def SourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # PV_AlarmState
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PV_AlarmState
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # PV_AlarmState
    def CaState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # PV_AlarmState
    def Severity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # PV_AlarmState
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def PV_AlarmStateStart(builder): builder.StartObject(6)
def Start(builder):
    return PV_AlarmStateStart(builder)
def PV_AlarmStateAddSourceName(builder, sourceName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sourceName), 0)
def AddSourceName(builder, sourceName):
    return PV_AlarmStateAddSourceName(builder, sourceName)
def PV_AlarmStateAddTimestamp(builder, timestamp): builder.PrependInt64Slot(1, timestamp, 0)
def AddTimestamp(builder, timestamp):
    return PV_AlarmStateAddTimestamp(builder, timestamp)
def PV_AlarmStateAddState(builder, state): builder.PrependInt16Slot(2, state, 0)
def AddState(builder, state):
    return PV_AlarmStateAddState(builder, state)
def PV_AlarmStateAddCaState(builder, caState): builder.PrependInt16Slot(3, caState, 0)
def AddCaState(builder, caState):
    return PV_AlarmStateAddCaState(builder, caState)
def PV_AlarmStateAddSeverity(builder, severity): builder.PrependInt16Slot(4, severity, 0)
def AddSeverity(builder, severity):
    return PV_AlarmStateAddSeverity(builder, severity)
def PV_AlarmStateAddMessage(builder, message): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(message), 0)
def AddMessage(builder, message):
    return PV_AlarmStateAddMessage(builder, message)
def PV_AlarmStateEnd(builder): return builder.EndObject()
def End(builder):
    return PV_AlarmStateEnd(builder)