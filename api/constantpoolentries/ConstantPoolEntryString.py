from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryString(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_STRING_INDEX = 1
        self.string_index = self.bytecode_recorder.getU2At(self.OFFSET_OF_STRING_INDEX)

    def get_raw_byte_length(self):
        return 3
