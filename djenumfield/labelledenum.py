from enum import Enum


class classproperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class LabelledEnum(Enum):
    def __new__(cls, *args):
        if not hasattr(cls, '_member_type_'):
            cls._member_type_, first_enum = cls.__class__._get_mixins_(cls.__bases__)
        value, label = args
        if cls._member_type_ is None:
            cls._member_type_ = object
        obj = cls._member_type_.__new__(cls, value)
        obj.label = label
        obj._value_ = value
        return obj

    @classproperty
    def _choices(cls):
        return [(x, x.label) for x in cls]


class LabelledIntEnum(int, LabelledEnum):
    pass


class LabelledUnicodeEnum(unicode, LabelledEnum):
    pass
