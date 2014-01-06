from django.test import SimpleTestCase

from .base import Constants


class TestConstants(SimpleTestCase):

    def test_too_few(self):
        """
        The value of each kwarg must be an iterable with exactly two items.
        """
        with self.assertRaises(ValueError):
            Constants(foo=('one',))

    def test_too_many(self):
        """
        The value of each kwarg must be an iterable with exactly two items.
        """
        with self.assertRaises(ValueError):
            Constants(foo=('one', 'two', 'three'))

    def test_conflicting_codename(self):
        """
        The codename must not conflict with an existing codename or method.
        """
        with self.assertRaises(AttributeError):
            Constants(choices=('2', 'two'))

    def test_choices(self):
        """.choices() should return a choices list in Django's format."""
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        self.assertListEqual(constants.choices(), [('1', 'one'), ('2', 'two')])

    def test_get_list(self):
        """.get_list() should return a list of constant values."""
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        self.assertListEqual(constants.get_list('foo', 'bar'), ['1', '2'])

    def test_get_list_bad_element(self):
        """
        .get_list() should raise an AttributeError if a constant with the
        requested codename does not exist.
        """
        constants = Constants(foo=('1', 'one'), bar=('2', 'two'))
        with self.assertRaises(AttributeError):
            constants.get_list('baz')
