from enum import Enum


class classproperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class LabelledEnum(Enum):
    """
    Base class that allows for the creation of an enum with a value and a label
    using tuples as the Enum values. Using the LabelledIntEnum for example:
        >>> from labelledenum import LabelledIntEnum
        >>> class MyChoices(LabelledIntEnum):
        ...     one = (1, 'The First Choice')
        ...     two = (2, 'The Second Choice')
        ...
        >>> MyChoices.one
        <MyChoices.one: 1>
        >>> MyChoices.one.label
        'The First Choice'
        >>> MyChoices.one.value
        1
    """
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
    """
    Base class that allows for the creation of an enum with an int value and a label
    using tuples as the Enum values. Example:
        >>> from labelledenum import LabelledIntEnum
        >>> class MyChoices(LabelledIntEnum):
        ...     one = (1, 'The First Choice')
        ...     two = (2, 'The Second Choice')
        ...
        >>> MyChoices.one
        <MyChoices.one: 1>
        >>> MyChoices.one.label
        'The First Choice'
        >>> MyChoices.one.value
        1
    """


class LabelledUnicodeEnum(unicode, LabelledEnum):
    """
    Base class that allows for the creation of an enum with a unicode value and a label
    using tuples as the Enum values. Example:
        >>> from labelledenum import LabelledUnicodeEnum
        >>> class MyChoices(LabelledUnicodeEnum):
        ...     one = ('one', 'The First Choice')
        ...     two = ('two', 'The Second Choice')
        ...
        >>> MyChoices.one
        <MyChoices.one: 'one'>
        >>> MyChoices.one.label
        'The First Choice'
        >>> MyChoices.one.value
        'one'
    """
