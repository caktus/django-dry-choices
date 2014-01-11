from unittest import TestCase

from ..base import Choices, C


class TestChoices(TestCase):

    def setUp(self):
        super(TestChoices, self).setUp()
        self.choices = Choices(
            C(codename='hello', value=1, description='First'),
            C(codename='world', value=2, description='Second'),
        )

    def test_invalid_codename(self):
        """Each codename must be a valid Python identifier."""
        args = [C(codename='9invalid', value=1, description='Invalid')]
        self.assertRaises(AttributeError, Choices, *args)

    def test_conflicting_codename(self):
        """Codename cannot conflict with an existing attribute."""
        args = [C(codename='get_choices', value=1, description='Conflicting')]
        self.assertRaises(AttributeError, Choices, *args)

    def test_duplicate_codename(self):
        """Codenames cannot be duplicated."""
        args = [
            C(codename='duplicate', value=1, description='Duplicated 1'),
            C(codename='duplicate', value=2, description='Duplicated 2'),
        ]
        self.assertRaises(AttributeError, Choices, *args)

    def test_initialization_formats(self):
        """Choices can be initialized in multiple ways."""
        choices = Choices(
            C(codename="one", value=1, description="You can use **kwargs"),
            C("two", 2, "You can use *args"),
            C("three", 3, description="You can mix *args and **kwargs"),
            ("four", 4, "You can use a 3-tuple"),
            ["five", 5, "You can use an iterable of length 3"],
        )
        codenames = ["one", "two", "three", "four", "five"]
        for value, codename in enumerate(codenames, start=1):
            self.assertEquals(getattr(choices, codename), value)

    def test_iteration(self):
        """Iteration is over the Django-style choices list."""
        result = [choice for choice in self.choices]
        expected = [(1, 'First'), (2, 'Second')]
        self.assertEquals(result, expected)

    def test_repr(self):
        """Smoke test for string representation."""
        result = str(self.choices)
        expected = "Choices[hello, world]"
        self.assertEquals(result, expected)

    def test_get_choices(self):
        """
        get_choices() should return a choices list in Django's format, in the
        order in which the choices were originally passed in.
        """
        result = self.choices.get_choices()
        expected = [(1, 'First'), (2, 'Second')]
        self.assertEquals(result, expected)

    def test_get_values(self):
        """get_values() should return a list of values."""
        result = self.choices.get_values('hello', 'world')
        expected = [1, 2]
        self.assertEquals(result, expected)

    def test_get_invalid_value(self):
        """AttributeError should occur when accessing a non-existant choice."""
        self.assertRaises(AttributeError, self.choices.get_values, 'invalid')
