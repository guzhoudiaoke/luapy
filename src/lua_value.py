from lua_type import LuaType


class LuaValue:
    @staticmethod
    def type_of(val):
        if val is None:
            return LuaType.NIL
        elif isinstance(val, bool):
            return LuaType.BOOLEAN
        elif isinstance(val, int) or isinstance(val, float):
            return LuaType.NUMBER
        elif isinstance(val, str):
            return LuaType.STRING
        raise Exception('Type not support')

    @staticmethod
    def to_boolean(val):
        if val is None:
            return False
        elif isinstance(val, bool):
            return val
        else:
            return True
