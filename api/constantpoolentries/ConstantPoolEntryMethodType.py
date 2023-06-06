from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryMethodType(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_DESCRIPTOR_INDEX = 1
        self.descriptorIndex = self.bytecode_recorder.getU2At(self.OFFSET_OF_DESCRIPTOR_INDEX)

    def get_raw_byte_length(self):
        return 3
