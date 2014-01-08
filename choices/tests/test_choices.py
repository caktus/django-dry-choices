from unittest import TestCase

from ..base import Choices, C


class TestChoices(TestCase):

    def test_invalid_codename(self):
        """Each codename must be a valid Python identifier."""
        with self.assertRaises(AttributeError):
            Choices(C(codename='9invalid', value=1, description='Invalid'))

    def test_conflicting_codename(self):
        """Codename cannot conflict with an existing attribute."""
        with self.assertRaises(AttributeError):
            Choices(C(codename='get_choices', value=1, description='Conflicting'))

    def test_duplicate_codename(self):
        """Codenames cannot be duplicated."""
        with self.assertRaises(AttributeError):
            Choices(
                C(codename='duplicate', value=1, description='Duplicated 1'),
                C(codename='duplicate', value=2, description='Duplicated 2'),
            )

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

    def test_get_choices(self):
        """
        get_choices() should return a choices list in Django's format, in the
        order in which the choices were originally passed in.
        """
        choices = Choices(
            C(codename='hello', value=1, description='First'),
            C(codename='world', value=2, description='Second'),
        )
        self.assertEquals(choices.get_choices(), [
            (1, 'First'),
            (2, 'Second'),
        ])

    def test_repr(self):
        """Smoke test for string representation."""
        str(Choices(C(codename='hello', value=1, description='Hello')))

    def test_get_values(self):
        choices = Choices(
            C(codename='hello', value=1, description='First'),
            C(codename='world', value=2, description='Second'),
        )
        self.assertEquals(choices.get_values('hello', 'world'), [1, 2])

    def test_get_invalid_value(self):
        choices = Choices(
            C(codename='hello', value=1, description='First'),
            C(codename='world', value=2, description='Second'),
        )
        with self.assertRaises(AttributeError):
            self.assertEquals(choices.get_values('invalid'))
