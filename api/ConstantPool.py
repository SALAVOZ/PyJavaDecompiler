

class ConstantPool:
    def __init__(self):
        self.CPT_UTF8 = 0
        self.CPT_Integer = 1
        self.CPT_Float = 2
        self.CPT_Long = 3
        self.CPT_Double = 4
        self.CPT_Class = 5
        self.CPT_String = 6
        self.CPT_FieldRef = 7
        self.CPT_MethodRef = 8
        self.CPT_InterfaceMethodRef = 9
        self.CPT_NameAndType = 10
        self.CPT_MethodHandle = 11
        self.CPT_MethodType = 12
        self.CPT_DynamicInfo = 13
        self.CPT_InvokeDynamic = 14
        self.CPT_ModuleInfo = 15
        self.CPT_PackageInfo = 16
        self.VAL_UTF8 = 1
        self.VAL_Integer = 3
        self.VAL_Float = 4
        self.VAL_Long = 5
        self.VAL_Double = 6
        self.VAL_Class = 7
        self.VAL_String = 8
        self.VAL_FieldRef = 9
        self.VAL_MethodRef = 10
        self.VAL_InterfaceMethodRef = 11
        self.VAL_NameAndType = 12
        self.VAL_MethodHandle = 15
        self.VAL_MethodType = 16
        self.VAL_DynamicInfo = 17
        self.VAL_InvokeDynamic = 18
        self.VAL_ModuleInfo = 19
        self.VAL_PackageInfo = 20

    def get(self, val: bytes):
        match val:
            case self.VAL_UTF8:
                return self.CPT_UTF8
            case self.VAL_Integer:
                return self.CPT_Integer
            case self.VAL_Float:
                return self.CPT_Float
            case self.VAL_Long:
                return self.CPT_Long
            case self.VAL_Double:
                return self.CPT_Double
            case self.VAL_Class:
                return self.CPT_Class
            case self.VAL_String:
                return self.CPT_String
            case self.VAL_FieldRef:
                return self.CPT_FieldRef
            case self.VAL_MethodRef:
                return self.CPT_MethodRef
            case self.VAL_InterfaceMethodRef:
                return self.CPT_InterfaceMethodRef
            case self.VAL_NameAndType:
                return self.CPT_NameAndType
            case self.VAL_MethodHandle:
                return self.CPT_MethodHandle
            case self.VAL_MethodType:
                return self.CPT_MethodType
            case self.VAL_DynamicInfo:
                return self.CPT_DynamicInfo
            case self.VAL_InvokeDynamic:
                return self.CPT_InvokeDynamic
            case self.VAL_ModuleInfo:
                return self.CPT_ModuleInfo
            case self.VAL_PackageInfo:
                return self.CPT_PackageInfo
            case _:
                raise ValueError("Invalid constant pool entry type : " + str(val))

    