from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryLong(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_REFERENCE_KIND = 1
        self.OFFSET_OF_REFERENCE_INDEX = 2

    def get_raw_byte_length(self):
        return 9
