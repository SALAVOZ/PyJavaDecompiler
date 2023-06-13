import enum


class AccessFlag(enum.StrEnum):
    ACC_PUBLIC = "public"
    ACC_PRIVATE = "private"
    ACC_PROTECTED = "protected"
    ACC_STATIC = "static"
    ACC_FINAL = "final"
    ACC_SUPER = "super"
    ACC_VOLATILE = "volatile"
    ACC_TRANSIENT = "transient"
    ACC_INTERFACE = "interface"
    ACC_ABSTRACT = "abstract"
    ACC_STRICT = "strictfp"
    ACC_SYNTHETIC = "/* synthetic */"
    ACC_ANNOTATION = "/* annotation */"
    ACC_ENUM = "/* enum */"
    ACC_MODULE = "/* module */"
    ACC_FAKE_SEALED = "sealed"
    ACC_FAKE_NON_SEALED = "non-sealed"

    @classmethod
    def get_access_flags(cls, raw: int):
        res = []
        if 0 != (raw & 0x1):
            res.append(cls.ACC_PUBLIC)
        if 0 != (raw & 0x2):
            res.append(cls.ACC_PRIVATE)
        if 0 != (raw & 0x4):
            res.append(cls.ACC_PROTECTED)
        if 0 != (raw & 0x8):
            res.append(cls.ACC_STATIC)
        if 0 != (raw & 0x10):
            res.append(cls.ACC_FINAL)
        if 0 != (raw & 0x20):
            res.append(cls.ACC_SUPER)
        if 0 != (raw & 0x40):
            res.append(cls.ACC_VOLATILE)
        if 0 != (raw & 0x80):
            res.append(cls.ACC_TRANSIENT)
        if 0 != (raw & 0x200):
            res.append(cls.ACC_INTERFACE)
        if 0 != (raw & 0x400):
            res.append(cls.ACC_ABSTRACT)
        if 0 != (raw & 0x1000):
            res.append(cls.ACC_SYNTHETIC)
        if 0 != (raw & 0x2000):
            res.append(cls.ACC_ANNOTATION)
        if 0 != (raw & 0x4000):
            res.append(cls.ACC_ENUM)
        if 0 != (raw & 0x8000):
            res.append(cls.ACC_MODULE)
        return res
