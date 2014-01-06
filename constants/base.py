from collections import namedtuple


class Constants(object):
    Constant = namedtuple('Constant', ['codename', 'value', 'description'])

    def __init__(self, **kwargs):
        self._constants = []
        for codename in kwargs:
            try:
                value, description = kwargs.get(codename)
            except (ValueError, TypeError):
                raise ValueError("Must pass in kwargs in format: "
                                 "**{'codename': (value, description)}")
            if hasattr(self, codename):
                raise AttributeError("'{0}' conflicts with an existing "
                                     "attribute.".format(codename))
            setattr(self, codename, value)
            c = self.Constant(codename, value, description)
            self._constants.append(c)

    def choices(self):
        """Django-style choices list to pass to a model or form field."""
        return [(c.value, c.description) for c in self._constants]

    def get_list(self, *codenames):
        """Returns a list of values corresponding with the codenames."""
        return [getattr(self, codename) for codename in codenames]
