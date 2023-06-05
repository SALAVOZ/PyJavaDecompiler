from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryInteger(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_BYTES = 1
        self.value = self.class_file.getS4At(self.OFFSET_OF_BYTES)

    def get_raw_byte_length(self):
        return 5
