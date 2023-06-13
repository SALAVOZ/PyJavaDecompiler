from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryInteger(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_BYTES = 1
        self.value = self.bytecode_recorder.getS4At(self.OFFSET_OF_BYTES)

    def get_raw_byte_length(self):
        return 5

    def __str__(self):
        return "CONSTANT_Integer value=" + str(self.value)
