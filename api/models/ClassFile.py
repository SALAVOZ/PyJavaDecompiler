from api.BytecodeRecorder import BytecodeRecorder
from api.ConstantPool import ConstantPool
from api.constantpoolentries.ConstantPoolEntryClass import ConstantPoolEntryClass
from api.constantpoolentries.AcessFlagEnum import AccessFlag
import struct


class ClassFile:
    def __init__(self, filename: str, bytecode):
        self.filename: str = filename
        self.bytecode = bytecode
        self.offset: int = 0
        self.OFFSET_OF_MAGIC = 0
        self.OFFSET_OF_MINOR = 4
        self.OFFSET_OF_MAJOR = 6
        self.OFFSET_OF_CONSTANT_POOL_COUNT = 8
        self.OFFSET_OF_CONSTANT_POOL = 10
        '''
        Парсим байткод
        '''
        self.magic = self.getS4At(self.OFFSET_OF_MAGIC)
        if self.magic != 0xCAFEBABE:
            raise ValueError('magic bytes are invalid!')
        self.minor = self.getU2At(self.OFFSET_OF_MINOR)
        self.major = self.getU2At(self.OFFSET_OF_MAJOR)
        self.constant_pool_count = self.getU2At(self.OFFSET_OF_CONSTANT_POOL_COUNT)
        self.constant_pool = ConstantPool()
        bytecode_recorder = BytecodeRecorder(bytecode=bytecode)
        self.constant_pool.process_row(bytecode_recorder=bytecode_recorder, count=self.constant_pool_count)
        self.OFFSET_OF_ACCESS_FLAGS = self.OFFSET_OF_CONSTANT_POOL + self.constant_pool.get_length()
        self.OFFSET_OF_THIS_CLASS = self.OFFSET_OF_ACCESS_FLAGS + 2
        self.OFFSET_OF_SUPER_CLASS = self.OFFSET_OF_THIS_CLASS + 2
        self.OFFSET_OF_INTERFACES_COUNT = self.OFFSET_OF_SUPER_CLASS + 2
        self.OFFSET_OF_INTERFACES = self.OFFSET_OF_INTERFACES_COUNT + 2
        self.interfaces_count = bytecode_recorder.getU2At(self.OFFSET_OF_INTERFACES_COUNT, from_zero=True)
        self.tmp_interfaces = self.get_interfaces(bytecode_recorder, self.OFFSET_OF_INTERFACES, self.interfaces_count)
        self.this_class = bytecode_recorder.getU2At(self.OFFSET_OF_THIS_CLASS, from_zero=True)
        access_flag_raw = bytecode_recorder.getU2At(self.OFFSET_OF_ACCESS_FLAGS, from_zero=True)
        self.access_flags = AccessFlag.get_access_flags(access_flag_raw)


    def get_bytecode(self):
        return self.bytecode

    def get_filename(self):
        return self.filename

    def getS4At(self, offset: int) -> int:
        """Возвращает первые 4 байта"""
        current_offset = self.get_offset()
        return (((self.bytecode[current_offset + offset] & 0xFF) << 24) |
                ((self.bytecode[current_offset + offset + 1] & 0xFF) << 16) |
                ((self.bytecode[current_offset + offset + 2] & 0xFF) << 8) |
                (self.bytecode[current_offset + offset + 3] & 0xFF))

    def getU2At(self, offset: int) -> int:
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

    def getS1At(self, offset: int) -> int:
        current_offset = self.get_offset()
        return self.bytecode[current_offset + offset]

    def get_bytes_at(self, count: int, offset: int) -> bytearray:
        current_offset = self.get_offset()
        res: bytearray = self.bytecode[current_offset + offset: current_offset + offset + count]
        return res

    def get_offset(self):
        return self.offset

    def add_current_offset(self, to_add: int):
        self.offset += to_add

    def get_interfaces(self, bytecode_recorder: BytecodeRecorder, interfaces_offset: int, interfaces_count: int) -> list[ConstantPoolEntryClass]:
        interfaces: list[ConstantPoolEntryClass] = []
        for _ in range(interfaces_count):
            bytecode_recorder.change_to_tmp_offset(interfaces_offset)
            offset: int = bytecode_recorder.getU2At(0)
            bytecode_recorder.add_current_offset(2)
            java_class = self.constant_pool.get_entry(offset)
            interfaces.append(java_class)
        return interfaces
