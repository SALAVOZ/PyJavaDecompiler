from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryInvokeDynamic(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_BOOTSTRAP_METHOD_ATTR_INDEX = 1
        self.OFFSET_OF_NAME_AND_TYPE_INDEX = 3
        self.bootstrapMethodAttrIndex = self.class_file.getU2At(self.OFFSET_OF_BOOTSTRAP_METHOD_ATTR_INDEX)
        self.nameAndTypeIndex = self.class_file.getU2At(self.OFFSET_OF_NAME_AND_TYPE_INDEX)

    def get_raw_byte_length(self):
        return 5