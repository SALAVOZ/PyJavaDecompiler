from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryMethodRef(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder, interface_method: bool):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_CLASS_INDEX = 1
        self.OFFSET_OF_NAME_AND_TYPE_INDEX = 3
        self.class_index = self.bytecode_recorder.getU2At(self.OFFSET_OF_CLASS_INDEX)
        self.name_and_type_index = self.bytecode_recorder.getU2At(self.OFFSET_OF_NAME_AND_TYPE_INDEX)
        self.interface_method = interface_method

    def get_raw_byte_length(self):
        return 5
