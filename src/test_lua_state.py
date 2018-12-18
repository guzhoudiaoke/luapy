from lua_state import LuaState


def main():
    ls = LuaState()

    ls.push_boolean(True)
    ls.dump()
    ls.push_integer(10)
    ls.dump()
    ls.push_nil()
    ls.dump()
    ls.push_string('hello')
    ls.dump()
    ls.push_value(-4)
    ls.dump()
    ls.replace(3)
    ls.dump()
    ls.set_top(6)
    ls.dump()
    ls.remove(-3)
    ls.dump()
    ls.set_top(-5)
    ls.dump()


if __name__ == '__main__':
    main()
