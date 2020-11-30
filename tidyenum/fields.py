"""
Various model fields that mostly provide default field sizes to ensure
these are consistant when used across multiple models.
"""

from django.db.models import CharField, IntegerField
from past.builtins import basestring
from builtins import str as text
import logging

log = logging.getLogger(__name__)


class EnumFieldMixin(object):
    """
    Mixin for handling Labelled Enum fields
    """

    def __init__(self, *args, **kwargs):
        try:
            # required to make south work
            self.enum = kwargs.pop('enum')
            choices = self.enum._choices
            defaults = {"choices": choices, 'default': choices[0][0]}
        except KeyError:
            self.enum = None
            defaults = {}

        if self.enum:
            try:
                default = kwargs.pop('default')
                try:
                    default = self.enum(default).value
                except ValueError:
                    pass

                defaults['default'] = default

            except KeyError:
                pass

        defaults.update(kwargs)
        super(EnumFieldMixin, self).__init__(*args, **defaults)

    def from_db_value(self, value, expression, connection, context):
        value = self.to_python(value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super(EnumFieldMixin, self).deconstruct()
        if self.enum:
            kwargs['enum'] = self.enum
        return name, path, args, kwargs

    def to_python(self, value):
        if self.enum is None:
            return value

        if isinstance(value, basestring):
            try:
                map = self.enum._member_map_
                all_values = text(value).split('.')
                test = all_values[-1]
                value = map[test]
            except (IndexError, KeyError):
                pass

        if isinstance(value, self.enum):
            return value

        try:
            value = self.enum._member_type_(value)
        except (ValueError, KeyError):
            pass

        try:
            value = self.enum(value)
        except ValueError:
            pass

        return value

    def get_prep_value(self, value):
        value = self.to_python(value)
        return super(EnumFieldMixin, self).get_prep_value(getattr(value, 'value', value))

    def formfield(self, **kwargs):
        defaults = dict(kwargs)
        if 'initial' in kwargs:
            value = kwargs['initial']
            defaults['initial'] = getattr(value, 'value', value)

        return super(EnumFieldMixin, self).formfield(**defaults)


class EnumCharField(EnumFieldMixin, CharField):
    """
    CharField where choices are handled by an enum

    Expects kwarg enum that is a LabelledEnum subclass
    """


class EnumIntegerField(EnumFieldMixin, IntegerField):
    """
    IntegerField wher choices are handled by an enum

    Expects kwarg enum that is a LabelledEnum subclass
    """
