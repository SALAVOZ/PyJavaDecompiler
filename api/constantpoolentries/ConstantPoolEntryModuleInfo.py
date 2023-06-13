from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryModuleInfo(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_NAME_INDEX = 1
        self.nameIndex = self.bytecode_recorder.getU2At(self.OFFSET_OF_NAME_INDEX)

    def get_raw_byte_length(self):
        return 3

    def __str__(self):
        return 'NameIndex value=' + str(self.nameIndex)
