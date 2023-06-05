from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryMethodRef(AbstractConstantPool):
    def __init__(self, class_file: ClassFile, interface_method: bool):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_CLASS_INDEX = 1
        self.OFFSET_OF_NAME_AND_TYPE_INDEX = 3
        self.class_index = self.class_file.getU2At(self.OFFSET_OF_CLASS_INDEX)
        self.name_and_type_index = self.class_file.getU2At(self.OFFSET_OF_NAME_AND_TYPE_INDEX)
        self.interface_method = interface_method

    def get_raw_byte_length(self):
        return 5
