from collections import namedtuple

from .utils import is_valid_identifier


__all__ = ['C', 'Choices']


# Encapsulates a single choice.
C = namedtuple('Choice', ['codename', 'value', 'description'])


class Choices(object):
    """Wrapper for a list of choices."""

    def __init__(self, *args):
        self._choices = []
        for item in args:
            if not isinstance(item, C):
                try:
                    codename, value, description = item
                except (ValueError, TypeError):
                    raise ValueError("Each choice must be a choices.C "
                                     "instance or a 3-tuple of the format "
                                     "(codename, value, description).")
                item = C(codename, value, description)
            if not is_valid_identifier(item.codename):
                raise AttributeError("The codename '{0}' is not a valid "
                                     "identifier.".format(item.codename))
            if hasattr(self, item.codename):
                raise AttributeError("The codename '{0}' conflicts with an "
                                     "existing attribute or is "
                                     "duplicated.".format(item.codename))
            setattr(self, item.codename, item.value)
            self._choices.append(item)

    def __repr__(self):
        clist = ', '.join(c.codename for c in self._choices)
        return u'Choices[{0}]'.format(clist)

    def get_choices(self):
        """Django-style choices list to pass to a model or form field."""
        return [(c.value, c.description) for c in self._choices]

    def get_values(self, *codenames):
        """Returns a list of values corresponding with the codenames."""
        return [getattr(self, codename) for codename in codenames]
