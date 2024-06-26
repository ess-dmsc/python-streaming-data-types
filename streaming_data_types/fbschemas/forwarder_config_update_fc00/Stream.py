# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Stream(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Stream()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStream(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def StreamBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x66\x63\x30\x30", size_prefixed=size_prefixed)

    # Stream
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Stream
    def Channel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Stream
    def Schema(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Stream
    def Topic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Stream
    def Protocol(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Stream
    def Periodic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def StreamStart(builder): builder.StartObject(5)
def Start(builder):
    return StreamStart(builder)
def StreamAddChannel(builder, channel): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(channel), 0)
def AddChannel(builder, channel):
    return StreamAddChannel(builder, channel)
def StreamAddSchema(builder, schema): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(schema), 0)
def AddSchema(builder, schema):
    return StreamAddSchema(builder, schema)
def StreamAddTopic(builder, topic): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(topic), 0)
def AddTopic(builder, topic):
    return StreamAddTopic(builder, topic)
def StreamAddProtocol(builder, protocol): builder.PrependUint16Slot(3, protocol, 0)
def AddProtocol(builder, protocol):
    return StreamAddProtocol(builder, protocol)
def StreamAddPeriodic(builder, periodic): builder.PrependInt32Slot(4, periodic, 0)
def AddPeriodic(builder, periodic):
    return StreamAddPeriodic(builder, periodic)
def StreamEnd(builder): return builder.EndObject()
def End(builder):
    return StreamEnd(builder)