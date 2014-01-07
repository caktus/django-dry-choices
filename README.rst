django-constants
================

django-constants provides a concise, consistent, and DRY way to define
constants for Django model and form choice fields.

:master: |master-status|

.. |master_status| image::
    https://api.travis-ci.org/caktus/django-constants.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/caktus/django-constants

Usage
-----

`Constants` are defined as follows::

    from django import models

    from constants import Constants, C


    class Foo(models.Model):
        STATUSES = Constants(
            C(codename='good', value='0', description='In good condition'),
            C(codename='okay', value='1', description='In okay condition'),
            C(codename='poor', value='2', description='In poor condition'),
        )

        status = models.CharField(max_length=1, choices=STATUSES.choices(),
                                  default=STATUSES.good)

Each constant passed to the initializer specifies a Pythonic codename, a
value, and a human-friendly description. You may also pass in constants as a
3-tuple of the format `(codename, value, description)`.

To pass the constants to the `choices` argument of a field, use the
`get_choices()` method of the `Constants` instance. Choices will be in the
same order as the constants were passed into the initializer.

Each codename is available directly on the `Constants` instance::

    >>> Foo.STATUSES.good
    '0'

Since the `Constants` class is only a wrapper, you can still use the built-in
`Model.get_X_display` method as usual::

    >>> bar = Foo.objects.create(status=Foo.STATUSES.okay)
    >>> bar.get_status_display()
    'In okay condition'

To get a sublist of constants, you can use the `get_values` method on a
`Constants` instance. The following two lines of code are equivalent::

    >>> acceptable = Foo.objects.filter(status__in=[Foo.STATUSES.good, Foo.STATUSES.okay])
    >>> acceptable = Foo.objects.filter(status__in=Foo.STATUSES.get_values('good', 'okay'))

`Constants` can be used for form fields as well::

    from django import forms

    from constants import Constants, C


    class FavoriteForm(forms.Form):
        COLORS = Constants(
            C(codename='red', value='r', description='Red'),
            C(codename='green', value='g', description='Green'),
            C(codename='blue', value='b', description='Blue'),
        )

        favorite_color = forms.ChoiceField(choices=COLORS.get_choices(),
                                           initial=COLORS.blue)


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
