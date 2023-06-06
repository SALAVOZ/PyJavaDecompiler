from api.BytecodeRecorder import BytecodeRecorder
from api.constantpoolentries.ConstantPoolEntryClass import ConstantPoolEntryClass
from api.constantpoolentries.ConstantPoolEntryDouble import ConstantPoolEntryDouble
from api.constantpoolentries.ConstantPoolEntryDynamicInfo import ConstantPoolEntryDynamicInfo
from api.constantpoolentries.ConstantPoolEntryFieldRef import ConstantPoolEntryFieldRef
from api.constantpoolentries.ConstantPoolEntryFloat import ConstantPoolEntryFloat
from api.constantpoolentries.ConstantPoolEntryInteger import ConstantPoolEntryInteger
from api.constantpoolentries.ConstantPoolEntryInvokeDynamic import ConstantPoolEntryInvokeDynamic
from api.constantpoolentries.ConstantPoolEntryLong import ConstantPoolEntryLong
from api.constantpoolentries.ConstantPoolEntryMethodHandle import ConstantPoolEntryMethodHandle
from api.constantpoolentries.ConstantPoolEntryMethodRef import ConstantPoolEntryMethodRef
from api.constantpoolentries.ConstantPoolEntryMethodType import ConstantPoolEntryMethodType
from api.constantpoolentries.ConstantPoolEntryModuleInfo import ConstantPoolEntryModuleInfo
from api.constantpoolentries.ConstantPoolEntryNameAndType import ConstantPoolEntryNameAndType
from api.constantpoolentries.ConstantPoolEntryPackageInfo import ConstantPoolEntryPackageInfo
from api.constantpoolentries.ConstantPoolEntryString import ConstantPoolEntryString
from api.constantpoolentries.ConstantPoolEntryUTF8 import ConstantPoolEntryUTF8
from api.constantpoolentries.AbstractConstantPoolEntry import AbstractConstantPool


class ConstantPool:
    def __init__(self):
        self.length: int = 0
        self.dynamic_constant = False
        self.constant_pool_entries: list[AbstractConstantPool] = []
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

    def get_length(self):
        return self.length

    def get(self, val: int):
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

    def process_row(self, bytecode_recorder: BytecodeRecorder, count: int) -> (list[AbstractConstantPool | None]):
        constant_pool_entries: list[AbstractConstantPool | None] = []
        dynamic_constant = False
        count -= 1
        bytecode_recorder.add_current_offset(bytecode_recorder.OFFSET_OF_CONSTANT_POOL)
        for x in range(count):
            b = bytecode_recorder.getS1At(0)
            cpe: AbstractConstantPool
            t = self.get(b)
            match t:
                case self.CPT_NameAndType:
                    cpe = ConstantPoolEntryNameAndType(bytecode_recorder)
                case self.CPT_String:
                    cpe = ConstantPoolEntryString(bytecode_recorder)
                case self.CPT_FieldRef:
                    cpe = ConstantPoolEntryFieldRef(bytecode_recorder)
                case self.CPT_MethodRef:
                    cpe = ConstantPoolEntryMethodRef(bytecode_recorder, False)
                case self.CPT_InterfaceMethodRef:
                    cpe = ConstantPoolEntryMethodRef(bytecode_recorder, True)
                case self.CPT_Class:
                    cpe = ConstantPoolEntryClass(bytecode_recorder)
                case self.CPT_Double:
                    cpe = ConstantPoolEntryDouble(bytecode_recorder)
                case self.CPT_Float:
                    cpe = ConstantPoolEntryFloat(bytecode_recorder)
                case self.CPT_Long:
                    cpe = ConstantPoolEntryLong(bytecode_recorder)
                case self.CPT_Integer:
                    cpe = ConstantPoolEntryInteger(bytecode_recorder)
                case self.CPT_UTF8:
                    cpe = ConstantPoolEntryUTF8(bytecode_recorder)
                case self.CPT_MethodHandle:
                    cpe = ConstantPoolEntryMethodHandle(bytecode_recorder)
                case self.CPT_MethodType:
                    cpe = ConstantPoolEntryMethodType(bytecode_recorder)
                case self.CPT_DynamicInfo:
                    cpe = ConstantPoolEntryDynamicInfo(bytecode_recorder)
                    dynamic_constant = True
                case self.CPT_InvokeDynamic:
                    cpe = ConstantPoolEntryInvokeDynamic(bytecode_recorder)
                case self.CPT_ModuleInfo:
                    cpe = ConstantPoolEntryModuleInfo(bytecode_recorder)
                case self.CPT_PackageInfo:
                    cpe = ConstantPoolEntryPackageInfo(bytecode_recorder)
                case _:
                    raise ValueError("Invalid constant pool entry : " + "")
            constant_pool_entries.append(cpe)
            match t:
                case self.CPT_Double:
                    pass
                case self.CPT_Long:
                    constant_pool_entries.append(None)
            cpe_length = cpe.get_raw_byte_length()
            bytecode_recorder.add_current_offset(cpe_length)
            self.length += cpe_length
        self.constant_pool_entries = constant_pool_entries
        self.dynamic_constant = dynamic_constant
        return constant_pool_entries

    def get_entry(self, index: int):
        if index > len(self.constant_pool_entries):
            raise ValueError("To big offset")
        return self.constant_pool_entries[index - 1]