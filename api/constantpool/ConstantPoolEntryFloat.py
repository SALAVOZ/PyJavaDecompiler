from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryFloat(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_CLASS_INDEX = 1
        self.OFFSET_OF_NAME_AND_TYPE_INDEX = 3
        self.classIndex: bytes = self.class_file.getU2At(self.OFFSET_OF_CLASS_INDEX)
        self.nameAndTypeIndex: bytes = self.class_file.getU2At(self.OFFSET_OF_NAME_AND_TYPE_INDEX)

    def get_raw_byte_length(self):
        return 4
