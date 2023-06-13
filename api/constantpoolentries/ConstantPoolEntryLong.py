from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryLong(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.value = self.bytecode_recorder.get_long_at()

    def get_raw_byte_length(self):
        return 9

    def __str__(self):
        return 'CONSTANT_Long[' + str(self.value) + ']'
