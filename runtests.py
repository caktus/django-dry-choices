#!/usr/bin/env python
import os
import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest


def get_suite():
    setup_dir = os.path.abspath(os.path.dirname(__file__))
    return unittest.defaultTestLoader.discover(setup_dir)


def runtests():
    suite = get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    runtests()
