import enum


class MethodHandleBehaviour(enum.IntEnum):
    GET_FIELD = 0
    GET_STATIC = 1
    PUT_FIELD = 2
    PUT_STATIC = 3
    INVOKE_VIRTUAL = 4
    INVOKE_STATIC = 5
    INVOKE_SPECIAL = 6
    NEW_INVOKE_SPECIAL = 7
    INVOKE_INTERFACE = 8

    @classmethod
    def decode(cls, value: bytes):
        match value:
            case 1:
                return cls.GET_FIELD
            case 2:
                return cls.GET_STATIC
            case 3:
                return cls.PUT_FIELD
            case 4:
                return cls.PUT_STATIC
            case 5:
                return cls.INVOKE_VIRTUAL
            case 6:
                return cls.INVOKE_STATIC
            case 7:
                return cls.INVOKE_SPECIAL
            case 8:
                return cls.NEW_INVOKE_SPECIAL
            case 9:
                return cls.INVOKE_INTERFACE
            case _:
                raise ValueError("error in methodHandleBehaviour...")
