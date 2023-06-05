import struct


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

    def getS4At(self, offset: int) -> bytes:
        """Возвращает первые 4 байта"""
        current_offset = self.get_offset()
        return (((self.bytecode[current_offset + offset] & 0xFF) << 24) |
                ((self.bytecode[current_offset + offset + 1] & 0xFF) << 16) |
                ((self.bytecode[current_offset + offset + 2] & 0xFF) << 8) |
                (self.bytecode[current_offset + offset + 3] & 0xFF))

    def getU2At(self, offset: int) -> bytes:
        """Возвращает 2 байта"""
        current_offset = self.get_offset()
        return (((self.bytecode[current_offset + offset] & 0xFF) << 8)
                | (self.bytecode[current_offset + offset + 1] & 0xFF))

    def get_double_at(self):
        long = self.get_long_at()
        long_int_binary = struct.pack('q', long)
        return struct.unpack('d', long_int_binary)[0]

    def get_float_at(self, offset):
        int_presentation = self.getS4At(offset)
        float_presentation = struct.unpack('f', struct.pack('i', int_presentation))[0]
        return float_presentation

    def get_long_at(self):
        current_offset = self.get_offset()
        return ((int(self.bytecode[current_offset + 0] & 0xFF) << 56) +
                (int(self.bytecode[current_offset + 1] & 0xFF) << 48) +
                (int(self.bytecode[current_offset + 2] & 0xFF) << 40) +
                (int(self.bytecode[current_offset + 3] & 0xFF) << 32) +
                (int(self.bytecode[current_offset + 4] & 0xFF) << 24) +
                ((self.bytecode[current_offset + 5] & 0xFF) << 16) +
                ((self.bytecode[current_offset + 6] & 0xFF) << 8) +
                ((self.bytecode[current_offset + 7] & 0xFF) << 0))

    def getS1At(self, offset: int) -> bytes:
        current_offset = self.get_offset()
        return self.bytecode[current_offset + offset]

    def get_offset(self):
        return self.offset

    def add_current_offset(self, to_add: int):
        self.offset += to_add
