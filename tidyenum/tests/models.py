from django.db.models import Model

from tidyenum.labelledenum import LabelledIntEnum, LabelledUnicodeEnum
from tidyenum.fields import EnumCharField, EnumIntegerField


class MyUnicodeChoice(LabelledUnicodeEnum):
    one = ('one', 'One')
    two = ('two', 'Two')


class MyIntChoice(LabelledIntEnum):
    one = (1, 'One')
    two = (2, 'Two')


class NeedingEnumChar(Model):
    status = EnumCharField(max_length=30, blank=False, null=False, enum=MyUnicodeChoice)


class EmptyDefaultEnumChar(Model):
    status = EnumCharField(max_length=30, default='', blank=False, null=False, enum=MyUnicodeChoice)


class EmptyEnumChar(Model):
    status = EnumCharField(max_length=30, default='', blank=False, null=False)


class NeedingEnumInteger(Model):
    status = EnumIntegerField(blank=False, null=False, enum=MyIntChoice)


class EmptyDefaultEnumInteger(Model):
    status = EnumIntegerField(default='', blank=False, null=False, enum=MyIntChoice)


class EmptyEnumInteger(Model):
    status = EnumIntegerField(default='', blank=False, null=False)
