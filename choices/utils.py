import re


__all__ = ['identifier_pattern', 'is_valid_identifier']


identifier_pattern = re.compile("^[a-zA-Z_][\w]*$")


# Returns whether a string is a valid Python identifier.
is_valid_identifier = lambda codename: bool(identifier_pattern.match(codename))
