from api.models.ClassFile import ClassFile
from abc import ABC, abstractmethod


class AbstractConstantPool(ABC):
    def __init__(self, class_file: ClassFile):
        self.OFFSET_OF_NAME_INDEX: int
        self.class_file: ClassFile = class_file

    @abstractmethod
    def get_raw_byte_length(self):
        pass
