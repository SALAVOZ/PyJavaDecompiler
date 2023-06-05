from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryPackageInfo(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_NAME_INDEX = 1
        self.name_index = self.class_file.getU2At(self.OFFSET_OF_NAME_INDEX)

    def get_raw_byte_length(self):
        return 3
