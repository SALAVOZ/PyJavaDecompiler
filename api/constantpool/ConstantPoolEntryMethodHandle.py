from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.constantpool.MethodHandleBehaviour import MethodHandleBehaviour
from api.models.ClassFile import ClassFile


class ConstantPoolEntryMethodHandle(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_REFERENCE_KIND = 1
        self.OFFSET_OF_REFERENCE_INDEX = 2
        self.referenceKind: MethodHandleBehaviour = MethodHandleBehaviour.decode(class_file.getS1At(self.OFFSET_OF_REFERENCE_KIND))
        self.referenceIndex = class_file.getU2At(self.OFFSET_OF_REFERENCE_INDEX)

    def get_raw_byte_length(self):
        return 9
