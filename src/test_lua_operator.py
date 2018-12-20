from lua_state import LuaState
from arith_op import ArithOp
from cmp_op import CmpOp


def main():
    ls = LuaState()

    ls.push_integer(1)
    ls.push_string('2.0')
    ls.push_string('3.0')
    ls.push_number(4.0)
    ls.dump()

    ls.arith(ArithOp.ADD)
    ls.dump()
    ls.arith(ArithOp.BNOT)
    ls.dump()

    ls.len(2)
    ls.dump()
    ls.concat(3)
    ls.dump()
    ls.push_boolean(ls.compare(1, CmpOp.EQ, 2))
    ls.dump()

    ls.push_number(2)
    ls.push_number(2)
    ls.dump()
    ls.arith(ArithOp.POW)
    ls.dump()

    ls.push_number(3.0)
    ls.push_boolean(ls.compare(4, CmpOp.LT, 5))
    ls.dump()

    ls.push_string('hello')
    ls.push_string('world')
    ls.push_boolean(ls.compare(7, CmpOp.LE, 8))
    ls.dump()


if __name__ == '__main__':
    main()
