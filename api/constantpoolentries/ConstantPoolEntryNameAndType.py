from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryNameAndType(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_NAME_INDEX = 1
        self.OFFSET_OF_DESCRIPTOR_INDEX = 3
        self.name_index = self.bytecode_recorder.getU2At(self.OFFSET_OF_NAME_INDEX)
        self.descriptor_index = self.bytecode_recorder.getU2At(self.OFFSET_OF_DESCRIPTOR_INDEX)

    def get_raw_byte_length(self):
        return 5

    def __str__(self):
        return "CONSTANT_NameAndType nameIndex=" + \
               str(self.name_index) + \
               ", descriptorIndex=" + \
               str(self.descriptor_index)
