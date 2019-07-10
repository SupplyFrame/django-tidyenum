from unittest import TestCase
from tidyenum.labelledenum import LabelledIntEnum, LabelledUnicodeEnum, LabelledEnum


class TestLabelledEnum(TestCase):

    def test_int_values_match(self):

        class MyChoice(LabelledIntEnum):
            one = (1, 'One')
            two = (2, 'Two')

        self.assertEqual(MyChoice.one, 1)
        self.assertEqual(MyChoice.two, 2)

        one = MyChoice.one

        self.assertEqual(MyChoice.one, one)
        self.assertEqual(one.label, 'One')

        self.assertEqual(one.one, one)
        self.assertNotEqual(one.two, one)

        self.assertEqual(MyChoice._choices, [(1, 'One'), (2, 'Two')])

        with self.assertRaises(AttributeError):
            ten = one.ten

    def test_str_values_match(self):

        class MyChoice(LabelledUnicodeEnum):
            one = ('one', 'One')
            two = ('two', 'Two')

        self.assertEqual(MyChoice.one, 'one')
        self.assertEqual(MyChoice.two, 'two')

        one = MyChoice.one

        try:
            self.assertTrue(isinstance(one, unicode))
        except:
            self.assertTrue(isinstance(one, str))

        self.assertEqual(MyChoice.one, one)
        self.assertEqual(one.label, 'One')

        self.assertEqual(MyChoice._choices, [('one', 'One'), ('two', 'Two')])
