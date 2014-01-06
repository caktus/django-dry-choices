from django.test import TestCase

from .base import Constants


class TestConstants(TestCase):

    def test_bad_format(self):
        with self.assertRaises(Exception):
            Constants(foo=('one',))
        with self.assertRaises(Exception):
            Constants(foo=('one', 'two', 'three'))

    def test_conflicting_codename(self):
        with self.assertRaises(Exception):
            Constants(choices=('2', 'two'))

    def test_choices(self):
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        choices = constants.choices()
        self.assertEquals(choices, [('1', 'one'), ('2', 'two')])

    def test_get_list(self):
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        clist = constants.get_list('foo', 'bar')
        self.assertEquals(clist, ['1', '2'])

    def test_get_list_bad_element(self):
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        with self.assertRaises(Exception):
            constants.get_list('foo', 'bar', 'baz')
