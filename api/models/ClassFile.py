

class ClassFile:
    def __init__(self, filename, bytecode):
        self.filename: str = filename
        self.bytecode = bytecode
        self.offset: int = 0
        self.OFFSET_OF_MAGIC = 0
        self.OFFSET_OF_MINOR = 4
        self.OFFSET_OF_MAJOR = 6
        self.OFFSET_OF_CONSTANT_POOL_COUNT = 8
        self.OFFSET_OF_CONSTANT_POOL = 10

    def get_bytecode(self):
        return self.bytecode

    def get_filename(self):
        return self.filename

    def getS4At(self, offset) -> bytes:
        """Возвращает первые 4 байта - magic bytes"""
        current_offset = self.get_offset()
        return (((self.bytecode[current_offset + offset] & 0xFF) << 24) |
                ((self.bytecode[current_offset + offset + 1] & 0xFF) << 16) |
                ((self.bytecode[current_offset + offset + 2] & 0xFF) << 8) |
                (self.bytecode[current_offset + offset + 3] & 0xFF))

    def getU2At(self, offset) -> bytes:
        """Возвращает 2 байта - minor и major"""
        current_offset = self.get_offset()
        return (((self.bytecode[current_offset + offset] & 0xFF) << 8)
                | (self.bytecode[current_offset + offset + 1] & 0xFF))

    def getS1At(self, offset) -> bytes:
        current_offset = self.get_offset()
        return self.bytecode[current_offset + offset]

    def get_offset(self):
        return self.offset

    def add_current_offset(self, to_add: int):
        self.offset += to_add
        