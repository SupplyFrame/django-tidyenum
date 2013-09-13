#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-tidyenum
------------

Tests for `django-tidyenum` labelledenum module.
"""

import unittest
from tidyenum import labelledenum


class LabelledEnum(unittest.TestCase):
    def test_int_values_match(self):

        class MyChoice(labelledenum.LabelledIntEnum):
            one = (1, 'One')
            two = (2, 'Two')

        self.assertEqual(MyChoice.one, 1)
        self.assertEqual(MyChoice.two, 2)

        one = MyChoice.one

        self.assertEqual(MyChoice.one, one)
        self.assertEqual(one.label, 'One')

        self.assertEqual(one.one, one)
        self.assertNotEqual(one.two, one)
        self.assertEqual(True, False)

        self.assertEqual(MyChoice._choices, [(1, 'One'), (2, 'Two')])

    def test_str_values_match(self):

        class MyChoice(labelledenum.LabelledUnicodeEnum):
            one = ('one', 'One')
            two = ('two', 'Two')

        self.assertEqual(MyChoice.one, 'one')
        self.assertEqual(MyChoice.two, 'two')

        one = MyChoice.one

        self.assertEqual(MyChoice.one, one)
        self.assertEqual(one.label, 'One')

        self.assertEqual(MyChoice._choices, [('one', 'One'), ('two', 'Two')])
