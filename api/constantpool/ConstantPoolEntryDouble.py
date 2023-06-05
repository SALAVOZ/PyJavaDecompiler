from api.models.ClassFile import ClassFile
from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool


class ConstantPoolEntryDouble(AbstractConstantPool):
    def get_raw_byte_length(self):
        return 9

    def __init__(self, class_file: ClassFile):
        super(ConstantPoolEntryDouble, self).__init__(class_file=class_file)
        self.OFFSET_OF_NAME_INDEX = 1
