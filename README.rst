django-choices |build_status|
===============================

.. |build_status| image::
    https://travis-ci.org/caktus/django-choices.png?branch=master
    :alt: Master build status
    :target: https://travis-ci.org/caktus/django-choices

django-choices provides a concise, consistent, and DRY way to define
choices for Django model and form choice fields.

Usage
-----

``Choices`` are defined as follows::

    from django import models
    from django.utils.translation import ugettext_lazy as _

    from choices import Choices, C


    class Foo(models.Model):
        STATUSES = Choices(
            C(codename='good', value='0', description=_('In good condition')),
            C(codename='okay', value='1', description=_('In okay condition')),
            C(codename='poor', value='2', description=_('In poor condition')),
        )

        status = models.CharField(max_length=1, choices=STATUSES.choices(),
                                  default=STATUSES.good)

Each choice passed to the initializer specifies a Pythonic *codename*, a
*value*, and a human-friendly *description* (which may optionally be
marked as a translation string). django-choices supports defining choices
in several different ways::

    >>> Choices(
        C(codename="one", value=1, description="You can use C(**kwargs)"),
        C("two", 2, "You can use C(*args)"),
        C("three", 3, description="You can mix C(*args, **kwargs)"),
        ("four", 4, "You can use a 3-tuple"),
        ["five", 5, "You can use any iterable of length 3"],
    )

To pass the choices to the ``choices`` argument of a Django model or form
field, use the ``get_choices()`` method of the ``Choices`` instance. Choices
will be in the same order as the choices were passed into the initializer.

Each codename is available directly on the ``Choices`` instance::

    >>> Foo.STATUSES.good
    '0'

Since the ``Choices`` class is only a wrapper, you can still use the
built-in ``Model.get_X_display`` method as usual::

    >>> bar = Foo.objects.create(status=Foo.STATUSES.okay)
    >>> bar.get_status_display()
    'In okay condition'

To get a sublist of choices, you can use the ``get_values`` method on a
``Choices`` instance. The following two lines of code are equivalent::

    >>> acceptable = Foo.objects.filter(status__in=[Foo.STATUSES.good, Foo.STATUSES.okay])
    >>> acceptable = Foo.objects.filter(status__in=Foo.STATUSES.get_values('good', 'okay'))

``Choices`` can be used for form fields as well::

    from django import forms

    from choices import Choices, C


    class FavoriteForm(forms.Form):
        COLORS = Choices(
            C(codename='red', value='r', description='Red'),
            C(codename='green', value='g', description='Green'),
            C(codename='blue', value='b', description='Blue'),
        )

        favorite_color = forms.ChoiceField(choices=COLORS.get_choices(),
                                           initial=COLORS.blue)

Running the Tests
-----------------

You can run the tests via::

    >>> python setup.py test

or::

    >>> python runtests.py

If you are using Python 2.6, you will need to install `unittest2
<https://pypi.python.org/pypi/unittest2>`_.

To run the tests against multiple versions of Python, install `tox
<https://pypi.python.org/pypi/tox>`_, move to the top directory of the repo,
and run::

    >>> tox

License
-------

django-choices is released under the BSD License. See the
`LICENSE <https://github.com/caktus/django-choices/blob/master/LICENSE>`_
file for more details.

Contributing
------------

If you think you've found a bug or are interested in contributing to this
project check out `django-choices on Github
<https://github.com/caktus/django-choices>`_.

Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com/services>`_.
