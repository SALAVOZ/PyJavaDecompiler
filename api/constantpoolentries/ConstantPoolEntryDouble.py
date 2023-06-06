from api.BytecodeRecorder import BytecodeRecorder
from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool


class ConstantPoolEntryDouble(AbstractConstantPool):
    def get_raw_byte_length(self):
        return 9

    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super(ConstantPoolEntryDouble, self).__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_NAME_INDEX = 1
        self.value = self.bytecode_recorder.get_double_at()
