from django.db.models import Model
from django.test import TestCase
from tidyenum.tests import models


class TestEnumCharField(TestCase):

    def test_init(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')
        self.assertEqual(len(enumchar1.choices), 2)
        self.assertEqual(enumchar1.default, models.MyUnicodeChoice.one)

        enumchar2 = models.EmptyDefaultEnumChar._meta.get_field('status')
        self.assertEqual(len(enumchar2.choices), 2)
        self.assertEqual(enumchar2.default, '')

        enumchar3 = models.EmptyEnumChar._meta.get_field('status')
        self.assertEqual(len(enumchar3.choices), 0)
        self.assertEqual(enumchar3.default, '')

    def test_deconstruct(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')
        name, path, args, kwargs = enumchar1.deconstruct()

        self.assertNotEqual(kwargs.get('enum'), None)
        self.assertEqual(len(kwargs.get('choices')), 2)
        self.assertEqual(kwargs.get('default'), models.MyUnicodeChoice.one)

    def test_get_prep_value(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')
        self.assertEqual(enumchar1.get_prep_value(models.MyUnicodeChoice.two), 'two')

    def test_formfield(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')
        self.assertEqual(enumchar1.formfield(initial=models.MyUnicodeChoice.two).initial, 'two')

    def test_to_python(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')
        enumchar2 = models.EmptyDefaultEnumChar._meta.get_field('status')
        enumchar3 = models.EmptyEnumChar._meta.get_field('status')

        self.assertEqual(enumchar1.to_python('one'), models.MyUnicodeChoice.one)
        self.assertEqual(enumchar1.to_python('fifty'), 'fifty')
        self.assertEqual(enumchar2.to_python(models.MyUnicodeChoice), "<enum 'MyUnicodeChoice'>")
        self.assertEqual(enumchar3.to_python(models.MyUnicodeChoice.two), models.MyUnicodeChoice.two)

    def test_from_db_value(self):
        enumchar1 = models.NeedingEnumChar._meta.get_field('status')

        self.assertEqual(enumchar1.from_db_value('one', expression=None, connection=None, context={}), models.MyUnicodeChoice.one)


class TestEnumIntegerField(TestCase):

    def test_init(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')
        self.assertEqual(len(enumint1.choices), 2)
        self.assertEqual(enumint1.default, models.MyIntChoice.one)

        enumint2 = models.EmptyDefaultEnumInteger._meta.get_field('status')
        self.assertEqual(len(enumint2.choices), 2)
        self.assertEqual(enumint2.default, '')

        enumint3 = models.EmptyEnumInteger._meta.get_field('status')
        self.assertEqual(len(enumint3.choices), 0)
        self.assertEqual(enumint3.default, '')

    def test_deconstruct(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')
        name, path, args, kwargs = enumint1.deconstruct()

        self.assertNotEqual(kwargs.get('enum'), None)
        self.assertEqual(len(kwargs.get('choices')), 2)
        self.assertEqual(kwargs.get('default'), models.MyIntChoice.one)

    def test_get_prep_value(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')
        self.assertEqual(enumint1.get_prep_value(models.MyIntChoice.two), 2)

    def test_formfield(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')
        self.assertEqual(enumint1.formfield(initial=models.MyIntChoice.two).initial, 2)

    def test_to_python(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')
        enumint2 = models.EmptyDefaultEnumInteger._meta.get_field('status')
        enumint3 = models.EmptyEnumInteger._meta.get_field('status')

        self.assertEqual(enumint1.to_python('one'), 1)
        self.assertEqual(enumint1.to_python('fifty'), 'fifty')
        self.assertEqual(enumint3.to_python(models.MyIntChoice.two), models.MyIntChoice.two)
        with self.assertRaises(TypeError):
            enumint2.to_python(models.MyIntChoice)

    def test_from_db_value(self):
        enumint1 = models.NeedingEnumInteger._meta.get_field('status')

        self.assertEqual(enumint1.from_db_value('one', expression=None, connection=None, context={}), models.MyIntChoice.one)
