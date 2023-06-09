from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryFloat(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_CLASS_INDEX = 1
        self.OFFSET_OF_NAME_AND_TYPE_INDEX = 3
        self.classIndex = self.bytecode_recorder.getU2At(self.OFFSET_OF_CLASS_INDEX)
        self.nameAndTypeIndex = self.bytecode_recorder.getU2At(self.OFFSET_OF_NAME_AND_TYPE_INDEX)

    def get_raw_byte_length(self):
        return 4
