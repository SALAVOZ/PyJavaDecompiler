from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryMethodType(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_DESCRIPTOR_INDEX = 1
        self.descriptorIndex = self.class_file.getU2At(self.OFFSET_OF_DESCRIPTOR_INDEX)

    def get_raw_byte_length(self):
        return 3
