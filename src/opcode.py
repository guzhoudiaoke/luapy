# OpMode
IABC = 0
IABx = 1
IAsBx = 2
IAx = 3

# OpArg
OpArgN = 0
OpArgU = 1
OpArgR = 2
OpArgK = 3


class OpCode:
    MOVE = 0
    LOADK = 1
    LOADKX = 2
    LOADBOOL = 3
    LOADNIL = 4
    GETUPVAL = 5
    GETTABUP = 6
    GETTABLE = 7
    SETTABUP = 8
    SETUPVAL = 9
    SETTABLE = 10
    NEWTABLE = 11
    SELF = 12
    ADD = 13
    SUB = 14
    MUL = 15
    MOD = 16
    POW = 17
    DIV = 18
    IDIV = 19
    BAND = 20
    BOR = 21
    BXOR = 22
    SHL = 23
    SHR = 24
    UNM = 25
    BNOT = 26
    NOT = 27
    LEN = 28
    CONCAT = 29
    JMP = 30
    EQ = 31
    LT = 32
    LE = 33
    TEST = 34
    TESTSET = 35
    CALL = 36
    TAILCALL = 37
    RETURN = 38
    FORLOOP = 39
    FORPREP = 40
    TFORCALL = 41
    TFORLOOP = 42
    SETLIST = 43
    CLOSURE = 44
    VARARG = 45
    EXTRAARG = 46

    def __init__(self, test_flag, set_a_flag, arg_b_mode, arg_c_mode, op_mode, name):
        self.test_flag = test_flag
        self.set_a_flag = set_a_flag
        self.arg_b_mode = arg_b_mode
        self.arg_c_mode = arg_c_mode
        self.op_mode = op_mode
        self.name = name


op_codes = [
    #      T  A  B       C       mode   name
    OpCode(0, 1, OpArgR, OpArgN, IABC,  "MOVE    "),  # R(A) := R(B)
    OpCode(0, 1, OpArgK, OpArgN, IABx,  "LOADK   "),  # R(A) := Kst(Bx)
    OpCode(0, 1, OpArgN, OpArgN, IABx,  "LOADKX  "),  # R(A) := Kst(extra arg)
    OpCode(0, 1, OpArgU, OpArgU, IABC,  "LOADBOOL"),  # R(A) := (bool)B; if (C) pc++
    OpCode(0, 1, OpArgU, OpArgN, IABC,  "LOADNIL "),  # R(A), R(A+1), ..., R(A+B) := nil
    OpCode(0, 1, OpArgU, OpArgN, IABC,  "GETUPVAL"),  # R(A) := UpValue[B]
    OpCode(0, 1, OpArgU, OpArgK, IABC,  "GETTABUP"),  # R(A) := UpValue[B][RK(C)]
    OpCode(0, 1, OpArgR, OpArgK, IABC,  "GETTABLE"),  # R(A) := R(B)[RK(C)]
    OpCode(0, 0, OpArgK, OpArgK, IABC,  "SETTABUP"),  # UpValue[A][RK(B)] := RK(C)
    OpCode(0, 0, OpArgU, OpArgN, IABC,  "SETUPVAL"),  # UpValue[B] := R(A)
    OpCode(0, 0, OpArgK, OpArgK, IABC,  "SETTABLE"),  # R(A)[RK(B)] := RK(C)
    OpCode(0, 1, OpArgU, OpArgU, IABC,  "NEWTABLE"),  # R(A) := {} (size = B,C)
    OpCode(0, 1, OpArgR, OpArgK, IABC,  "SELF    "),  # R(A+1) := R(B); R(A) := R(B)[RK(C)]
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "ADD     "),  # R(A) := RK(B) + RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "SUB     "),  # R(A) := RK(B) - RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "MUL     "),  # R(A) := RK(B) * RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "MOD     "),  # R(A) := RK(B) % RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "POW     "),  # R(A) := RK(B) ^ RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "DIV     "),  # R(A) := RK(B) / RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "IDIV    "),  # R(A) := RK(B) // RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "BAND    "),  # R(A) := RK(B) & RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "BOR     "),  # R(A) := RK(B) | RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "BXOR    "),  # R(A) := RK(B) ~ RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "SHL     "),  # R(A) := RK(B) << RK(C)
    OpCode(0, 1, OpArgK, OpArgK, IABC,  "SHR     "),  # R(A) := RK(B) >> RK(C)
    OpCode(0, 1, OpArgR, OpArgN, IABC,  "UNM     "),  # R(A) := -R(B)
    OpCode(0, 1, OpArgR, OpArgN, IABC,  "BNOT    "),  # R(A) := ~R(B)
    OpCode(0, 1, OpArgR, OpArgN, IABC,  "NOT     "),  # R(A) := not R(B)
    OpCode(0, 1, OpArgR, OpArgN, IABC,  "LEN     "),  # R(A) := length of R(B)
    OpCode(0, 1, OpArgR, OpArgR, IABC,  "CONCAT  "),  # R(A) := R(B).. ... ..R(C)
    OpCode(0, 0, OpArgR, OpArgN, IAsBx, "JMP     "),  # pc+=sBx; if (A) close all upvalues >= R(A - 1)
    OpCode(1, 0, OpArgK, OpArgK, IABC,  "EQ      "),  # if ((RK(B) == RK(C)) ~= A) then pc++
    OpCode(1, 0, OpArgK, OpArgK, IABC,  "LT      "),  # if ((RK(B) <  RK(C)) ~= A) then pc++
    OpCode(1, 0, OpArgK, OpArgK, IABC,  "LE      "),  # if ((RK(B) <= RK(C)) ~= A) then pc++
    OpCode(1, 0, OpArgN, OpArgU, IABC,  "TEST    "),  # if not (R(A) <=> C) then pc++
    OpCode(1, 1, OpArgR, OpArgU, IABC,  "TESTSET "),  # if (R(B) <=> C) then R(A) := R(B) else pc++
    OpCode(0, 1, OpArgU, OpArgU, IABC,  "CALL    "),  # R(A), ...,R(A+C-2) := R(A)(R(A+1), ...,R(A+B-1))
    OpCode(0, 1, OpArgU, OpArgU, IABC,  "TAILCALL"),  # return R(A)(R(A+1), ... ,R(A+B-1))
    OpCode(0, 0, OpArgU, OpArgN, IABC,  "RETURN  "),  # return R(A), ... ,R(A+B-2)
    OpCode(0, 1, OpArgR, OpArgN, IAsBx, "FORLOOP "),  # R(A)+=R(A+2); if R(A) <?= R(A+1) then { pc+=sBx; R(A+3)=R(A) }
    OpCode(0, 1, OpArgR, OpArgN, IAsBx, "FORPREP "),  # R(A)-=R(A+2); pc+=sBx
    OpCode(0, 0, OpArgN, OpArgU, IABC,  "TFORCALL"),  # R(A+3), ... ,R(A+2+C) := R(A)(R(A+1), R(A+2));
    OpCode(0, 1, OpArgR, OpArgN, IAsBx, "TFORLOOP"),  # if R(A+1) ~= nil then { R(A)=R(A+1); pc += sBx }
    OpCode(0, 0, OpArgU, OpArgU, IABC,  "SETLIST "),  # R(A)[(C-1)*FPF+i] := R(A+i), 1 <= i <= B
    OpCode(0, 1, OpArgU, OpArgN, IABx,  "CLOSURE "),  # R(A) := closure(KPROTO[Bx])
    OpCode(0, 1, OpArgU, OpArgN, IABC,  "VARARG  "),  # R(A), R(A+1), ..., R(A+B-2) = vararg
    OpCode(0, 0, OpArgU, OpArgU, IAx,   "EXTRAARG"),  # extra (larger) argument for previous opcode
]


class Instruction:
    MAXARG_Bx = 1 << 18 - 1
    MAXARG_sBx = MAXARG_Bx >> 1

    def __init__(self, code):
        self.code = code

    def op_code(self):
        return self.code & 0x3f

    def a_b_c(self):
        return (self.code >> 6) & 0xff, (self.code >> 23) & 0x1ff, (self.code >> 14) & 0x1ff

    def a_bx(self):
        return (self.code >> 6) & 0xff, (self.code >> 14)

    def as_bx(self):
        a, bx = self.a_bx()
        return a, bx - Instruction.MAXARG_sBx

    def ax(self):
        return self.code >> 6

    def op_name(self):
        return op_codes[self.op_code()].name

    def op_mode(self):
        return op_codes[self.op_code()].op_mode

    def arg_b_mode(self):
        return op_codes[self.op_code()].arg_b_mode

    def arg_c_mode(self):
        return op_codes[self.op_code()].arg_c_mode

    def dump(self):
        print(self.op_name(), end=' ')
        if self.op_mode() == IABC:
            a, b, c = self.a_b_c()
            print('%8d' % a, end='')
            if self.arg_b_mode() != OpArgN:
                if b > 0xff:
                    print(' %8d' % (-1 - (b & 0xff)), end='')
                else:
                    print(' %8d' % b, end='')
            if self.arg_c_mode() != OpArgN:
                if c > 0xff:
                    print(' %8d' % (-1 - (c & 0xff)), end='')
                else:
                    print(' %8d' % c, end='')
        elif self.op_mode() == IABx:
            a, bx = self.a_bx()
            print('%8d' % a, end='')
            if self.arg_b_mode() == OpArgK:
                print(' %8d' % (-1 - bx), end='')
            elif self.arg_b_mode() == OpArgU:
                print(' %8d' % bx, end='')
        elif self.op_mode() == IAsBx:
            a, sbx = self.as_bx()
            print('%8d %8d' % (a, sbx), end='')
        elif self.op_mode() == IAx:
            ax = self.ax()
            print('%8d' % (-1 - ax), end='')
        print()
