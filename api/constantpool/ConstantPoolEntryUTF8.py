from api.constantpool.AbstractConstantPoolEntry import AbstractConstantPool
from api.models.ClassFile import ClassFile


class ConstantPoolEntryUTF8(AbstractConstantPool):
    def __init__(self, class_file: ClassFile):
        super().__init__(class_file=class_file)
        self.OFFSET_OF_LENGTH = 1
        self.OFFSET_OF_DATA = 3
        self.length: int = self.class_file.getU2At(self.OFFSET_OF_LENGTH)
        self.bytes = self.class_file.get_bytes_at(self.length, self.OFFSET_OF_DATA)
        self.out_chars: list[str] = ['' for _ in range(len(bytes))]
        self.tmp_value: str
        out: int = 0
        try:
            for curr_pos in range(0, len(self.bytes)):
                x = self.bytes[curr_pos]
                if (x & 0x80) == 0:
                    out += 1
                    self.out_chars[out] = chr(x)
                elif (x & 0xE0) == 0xC0:
                    curr_pos += 1
                    y = self.bytes[curr_pos]
                    if (y & 0xC0) == 0x80:
                        val = ((x & 0x1f) << 6) + y & 0x3f
                        out += 1
                        self.out_chars[out] = chr(val)
                elif (x & 0xF0) == 0xE0:
                    curr_pos += 1
                    y = self.bytes[curr_pos]
                    curr_pos += 1
                    z = self.bytes[curr_pos]
                    if (y & 0xC0) == 0x80 and (z & 0xC0) == 0x80:
                        val = ((x & 0xf) << 12) + ((y & 0x3f) << 6) + (z & 0x3f)
                        out += 1
                        self.out_chars[out] = chr(val)
            tmp_value = ''.join(self.out_chars)
        except:
            raise ValueError("ConstantPoolEntryUTF8")
        if tmp_value is None:
            tmp_value = str(self.bytes)
        self.value = tmp_value

    def get_raw_byte_length(self):
        return 3 + self.length
