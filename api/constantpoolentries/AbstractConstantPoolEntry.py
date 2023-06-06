from api.BytecodeRecorder import BytecodeRecorder
from abc import ABC, abstractmethod


class AbstractConstantPool(ABC):
    def __init__(self, bytecode_recorder: BytecodeRecorder):
        self.OFFSET_OF_NAME_INDEX: int
        self.bytecode_recorder: BytecodeRecorder = bytecode_recorder

    @abstractmethod
    def get_raw_byte_length(self):
        pass
