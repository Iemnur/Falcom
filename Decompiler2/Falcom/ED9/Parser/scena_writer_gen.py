from Falcom.ED9.Parser.scena_writer import _gScena, ScenaFunctionWrapper

sint8 = int
uint8 = int
sint16 = int
uint16 = int
sint32 = int
uint32 = int
float32 = float | int

def PUSH(arg1: int | float | str):
    return _gScena.handleOpCode(0x00, arg1)

def OP_00(arg1: int | float | str):
    return _gScena.handleOpCode(0x00, arg1)

def POP(arg1: uint8):
    # 0x01
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x01, arg1)

def OP_01(arg1: uint8):
    # 0x01
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x01, arg1)

def LOAD_STACK(arg1: sint32):
    # 0x02
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x02, arg1)

def OP_02(arg1: sint32):
    # 0x02
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x02, arg1)

def LOAD_STACK_DEREF(arg1: sint32):
    # 0x03
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x03, arg1)

def OP_03(arg1: sint32):
    # 0x03
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x03, arg1)

def PUSH_STACK_OFFSET(arg1: sint32):
    # 0x04
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x04, arg1)

def OP_04(arg1: sint32):
    # 0x04
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x04, arg1)

def POP_TO(arg1: sint32):
    # 0x05
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x05, arg1)

def OP_05(arg1: sint32):
    # 0x05
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x05, arg1)

def POP_TO_DEREF(arg1: sint32):
    # 0x06
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x06, arg1)

def OP_06(arg1: sint32):
    # 0x06
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x06, arg1)

def LOAD_GLOBAL(arg1: sint32):
    # 0x07
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x07, arg1)

def OP_07(arg1: sint32):
    # 0x07
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x07, arg1)

def SET_GLOBAL(arg1: sint32):
    # 0x08
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x08, arg1)

def OP_08(arg1: sint32):
    # 0x08
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x08, arg1)

def GET_REG(arg1: uint8):
    # 0x09
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x09, arg1)

def OP_09(arg1: uint8):
    # 0x09
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x09, arg1)

def SET_REG(arg1: uint8):
    # 0x0A
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x0A, arg1)

def OP_0A(arg1: uint8):
    # 0x0A
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x0A, arg1)

def JMP(arg1: str):
    # 0x0B
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0B, arg1)

def OP_0B(arg1: str):
    # 0x0B
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0B, arg1)

def CALL(arg1: uint16 | ScenaFunctionWrapper):
    # 0x0C
    assert isinstance(arg1, uint16 | ScenaFunctionWrapper)
    _gScena.handleOpCode(0x0C, arg1)

def OP_0C(arg1: uint16 | ScenaFunctionWrapper):
    # 0x0C
    assert isinstance(arg1, uint16 | ScenaFunctionWrapper)
    _gScena.handleOpCode(0x0C, arg1)

def RETURN():
    # 0x0D
    _gScena.handleOpCode(0x0D)

def OP_0D():
    # 0x0D
    _gScena.handleOpCode(0x0D)

def POP_JMP_NOT_ZERO(arg1: str):
    # 0x0E
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0E, arg1)

def OP_0E(arg1: str):
    # 0x0E
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0E, arg1)

def POP_JMP_ZERO(arg1: str):
    # 0x0F
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0F, arg1)

def OP_0F(arg1: str):
    # 0x0F
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x0F, arg1)

def ADD():
    # 0x10
    _gScena.handleOpCode(0x10)

def OP_10():
    # 0x10
    _gScena.handleOpCode(0x10)

def SUB():
    # 0x11
    _gScena.handleOpCode(0x11)

def OP_11():
    # 0x11
    _gScena.handleOpCode(0x11)

def MUL():
    # 0x12
    _gScena.handleOpCode(0x12)

def OP_12():
    # 0x12
    _gScena.handleOpCode(0x12)

def DIV():
    # 0x13
    _gScena.handleOpCode(0x13)

def OP_13():
    # 0x13
    _gScena.handleOpCode(0x13)

def MOD():
    # 0x14
    _gScena.handleOpCode(0x14)

def OP_14():
    # 0x14
    _gScena.handleOpCode(0x14)

def EQ():
    # 0x15
    _gScena.handleOpCode(0x15)

def OP_15():
    # 0x15
    _gScena.handleOpCode(0x15)

def NE():
    # 0x16
    _gScena.handleOpCode(0x16)

def OP_16():
    # 0x16
    _gScena.handleOpCode(0x16)

def GT():
    # 0x17
    _gScena.handleOpCode(0x17)

def OP_17():
    # 0x17
    _gScena.handleOpCode(0x17)

def GE():
    # 0x18
    _gScena.handleOpCode(0x18)

def OP_18():
    # 0x18
    _gScena.handleOpCode(0x18)

def LT():
    # 0x19
    _gScena.handleOpCode(0x19)

def OP_19():
    # 0x19
    _gScena.handleOpCode(0x19)

def LE():
    # 0x1A
    _gScena.handleOpCode(0x1A)

def OP_1A():
    # 0x1A
    _gScena.handleOpCode(0x1A)

def BITWISE_AND():
    # 0x1B
    _gScena.handleOpCode(0x1B)

def OP_1B():
    # 0x1B
    _gScena.handleOpCode(0x1B)

def BITWISE_OR():
    # 0x1C
    _gScena.handleOpCode(0x1C)

def OP_1C():
    # 0x1C
    _gScena.handleOpCode(0x1C)

def LOGICAL_AND():
    # 0x1D
    _gScena.handleOpCode(0x1D)

def OP_1D():
    # 0x1D
    _gScena.handleOpCode(0x1D)

def LOGICAL_OR():
    # 0x1E
    _gScena.handleOpCode(0x1E)

def OP_1E():
    # 0x1E
    _gScena.handleOpCode(0x1E)

def NEG():
    # 0x1F
    _gScena.handleOpCode(0x1F)

def OP_1F():
    # 0x1F
    _gScena.handleOpCode(0x1F)

def EZ():
    # 0x20
    _gScena.handleOpCode(0x20)

def OP_20():
    # 0x20
    _gScena.handleOpCode(0x20)

def NOT():
    # 0x21
    _gScena.handleOpCode(0x21)

def OP_21():
    # 0x21
    _gScena.handleOpCode(0x21)

def CALL_MODULE(arg1: sint32 | float | str, arg2: sint32 | float | str, arg3: uint8):
    # 0x22
    assert isinstance(arg1, sint32 | float | str)
    assert isinstance(arg2, sint32 | float | str)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x22, arg1, arg2, arg3)

def OP_22(arg1: sint32 | float | str, arg2: sint32 | float | str, arg3: uint8):
    # 0x22
    assert isinstance(arg1, sint32 | float | str)
    assert isinstance(arg2, sint32 | float | str)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x22, arg1, arg2, arg3)

def CALL_MODULE_NO_RETURN(arg1: sint32 | float | str, arg2: sint32 | float | str, arg3: uint8):
    # 0x23
    assert isinstance(arg1, sint32 | float | str)
    assert isinstance(arg2, sint32 | float | str)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x23, arg1, arg2, arg3)

def OP_23(arg1: sint32 | float | str, arg2: sint32 | float | str, arg3: uint8):
    # 0x23
    assert isinstance(arg1, sint32 | float | str)
    assert isinstance(arg2, sint32 | float | str)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x23, arg1, arg2, arg3)

def SYSCALL(arg1: uint8, arg2: uint8, arg3: uint8):
    # 0x24
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x24, arg1, arg2, arg3)

def OP_24(arg1: uint8, arg2: uint8, arg3: uint8):
    # 0x24
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x24, arg1, arg2, arg3)

def PUSH_CALLER_CONTEXT(arg1: str):
    # 0x25
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x25, arg1)

def OP_25(arg1: str):
    # 0x25
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x25, arg1)

def DEBUG_SET_LINENO(arg1: uint16):
    # 0x26
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x26, arg1)

def OP_26(arg1: uint16):
    # 0x26
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x26, arg1)

def POPN(arg1: uint8):
    # 0x27
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x27, arg1)

def OP_27(arg1: uint8):
    # 0x27
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x27, arg1)

def DEBUG_LOG(arg1: uint32):
    # 0x28
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x28, arg1)

def OP_28(arg1: uint32):
    # 0x28
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x28, arg1)

def PUSH_INT(arg1: sint32):
    # 0x1000
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x1000, arg1)

def OP_1000(arg1: sint32):
    # 0x1000
    assert isinstance(arg1, sint32)
    _gScena.handleOpCode(0x1000, arg1)

def PUSH_FLOAT(arg1: float32):
    # 0x1001
    assert isinstance(arg1, float32)
    _gScena.handleOpCode(0x1001, arg1)

def OP_1001(arg1: float32):
    # 0x1001
    assert isinstance(arg1, float32)
    _gScena.handleOpCode(0x1001, arg1)

def PUSH_STR(arg1: str):
    # 0x1002
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x1002, arg1)

def OP_1002(arg1: str):
    # 0x1002
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x1002, arg1)

def PUSH_FUNC_ID(arg1: uint16 | ScenaFunctionWrapper):
    # 0x1003
    assert isinstance(arg1, uint16 | ScenaFunctionWrapper)
    _gScena.handleOpCode(0x1003, arg1)

def OP_1003(arg1: uint16 | ScenaFunctionWrapper):
    # 0x1003
    assert isinstance(arg1, uint16 | ScenaFunctionWrapper)
    _gScena.handleOpCode(0x1003, arg1)

def PUSH_RET_ADDR(arg1: str):
    # 0x1004
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x1004, arg1)

def OP_1004(arg1: str):
    # 0x1004
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x1004, arg1)

def PUSH_CURRENT_FUNC_ID(arg1: uint32):
    # 0x1005
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x1005, arg1)

def OP_1005(arg1: uint32):
    # 0x1005
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x1005, arg1)

def MLIL_STUB():
    # 0x5000
    _gScena.handleOpCode(0x5000)

def OP_5000():
    # 0x5000
    _gScena.handleOpCode(0x5000)
