django-constants
================

django-constants provides a concise, consistent, and DRY way to define
constants for Django model and form choice fields.


Usage
-----

`Constants` are defined as follows::

    from django import models

    from constants import Constants


    class Foo(models.Model):
        STATUSES = Constants(
            good=('0', 'In good condition'),
            okay=('1', 'In okay condition'),
            poor=('2', 'In poor condition'),
        )

        status = models.CharField(max_length=1, choices=STATUSES.choices(),
                                  default=STATUSES.good)

Constants are passed to the initializer as keyword arguments. For each
keyword argument, the keyword is a codename for the constant, and the value is
a 2-tuple of the form `(value, description)` where the first element is the
value of the constant and the second element is a human-readable description.
To pass the constants to the `choices` argument of a field, use the
`choices()` method of the `Constants` instance.

Each codename is available directly on the `Constants` instance::

    >>> Foo.STATUSES.good
    '0'

Since the `Constants` class is only a wrapper, you can still use the built-in
`Model.get_X_display` method::

    >>> bar = Foo.objects.create(status=Foo.STATUSES.okay)
    >>> bar.get_status_display()
    'In okay condition'

To get a sublist of constants, you can use the `get_list` method on a
`Constants` instance. The following two lines of code are equivalent::

    >>> acceptable = Foo.objects.filter(status__in=[Foo.STATUSES.good, Foo.STATUSES.okay])
    >>> acceptable = Foo.objects.filter(status__in=Foo.STATUSES.get_list('good', 'okay'))

`Constants` can be used for form fields as well::

    from django import forms

    from constants import Constants


    class FavoriteForm(forms.Form):
        COLORS = Constants(
            red=('r', 'Red'),
            green=('g', 'Green'),
            blue=('b', 'Blue'),
        )

        favorite_color = forms.ChoiceField(choices=COLORS.choices())


Running the Tests
-----------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py


License
-------

django-constants is released under the BSD License. See the
`LICENSE <https://github.com/caktus/django-constants/blob/master/LICENSE>`_
file for more details.


Contributing
------------

If you think you've found a bug or are interested in contributing to this
project check out `django-constants on Github
<https://github.com/caktus/django-constants>`_.

Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com/services>`_.
