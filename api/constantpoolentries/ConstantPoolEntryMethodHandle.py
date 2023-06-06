from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool
from api.constantpoolentries.MethodHandleBehaviour import MethodHandleBehaviour
from api.BytecodeRecorder import BytecodeRecorder


class ConstantPoolEntryMethodHandle(AbstractConstantPool):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        super().__init__(bytecode_recorder=bytecode_recorder)
        self.OFFSET_OF_REFERENCE_KIND = 1
        self.OFFSET_OF_REFERENCE_INDEX = 2
        self.referenceKind: MethodHandleBehaviour = MethodHandleBehaviour.decode(self.bytecode_recorder.getS1At(self.OFFSET_OF_REFERENCE_KIND))
        self.referenceIndex = bytecode_recorder.getU2At(self.OFFSET_OF_REFERENCE_INDEX)

    def get_raw_byte_length(self):
        return 4
