from django.test import SimpleTestCase

from .. import utils


class TestIsValidIdentifier(SimpleTestCase):
    """Tests for constants.utils.is_valid_identifier."""

    def test_valid_identifiers(self):
        expected_valids = ['_hello_', '__hello__', 'hello1', 'hello']

        invalids = [identifier for identifier in expected_valids
                    if not utils.is_valid_identifier(identifier)]
        if invalids:
            self.fail("These identifiers should be valid but were not: " +
                      ", ".join("'{0}'".format(i) for i in invalids))

    def test_invalid_identifiers(self):
        expected_invalids = ['hello world', '1hello', ' hello', 'hello,world',
                             'hello-world']

        valids = [identifier for identifier in expected_invalids
                  if utils.is_valid_identifier(identifier)]
        if valids:
            self.fail("These identifiers should be invalid but were not: " +
                      ", ".join("'{0}'".format(i) for i in valids))
