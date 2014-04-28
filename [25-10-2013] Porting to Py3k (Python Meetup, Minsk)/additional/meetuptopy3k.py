# -*- coding: utf-8 -*-

import itertools
from abc import ABCMeta

__all__ = (
    'example1',
    'example2',
    'example3',
    'example4',
    'example5',
    'example6',
    'example7',
    'example8',
    'example9',
    'example10',
)


def example1():
    # sentry/__init__.py
    try:
        VERSION = __import__('pkg_resources').get_distribution('sentry').version
    except Exception, e:
        VERSION = 'unknown'


def example2():
    # sentry/management/commands/repair.py
    print u'Creating missing project keys'


def example3():
    value = 42

    # sentry/manager.py
    value = unicode(value)


def example4():
    LOG_LEVELS = {
        'some_key1': 'some_value1',
        'some_key2': 'some_value2',
    }

    # sentry/coreapi.py
    LOG_LEVEL_REVERSE_MAP = dict((v, k) for k, v in LOG_LEVELS.iteritems())


def example5():
    results = [1, 2, 3, 4,]
    tag_list = results

    # sentry/web/forms/accounts.py
    for i in xrange(len(results)): pass
    # sentry/web/forms/projects.py
    for k in itertools.imap(unicode, tag_list): pass


def example6():
    kwargs = {
        'some_key1': 'some_value1',
        'some_key2': 'some_value2',
    }

    # sentry/db/models/manager.py
    key, value = kwargs.items()[0]


def example7():
    k = 'some_string'
    value = k

    # sentry/coreapi.py
    if not isinstance(k, basestring): pass
    # sentry/web/forms/fields.py
    if isinstance(value, (int, long)): pass


def example8():
    access_or_func = lambda: 42

    # sentry/web/decorators.py
    if callable(access_or_func): pass


def example9():
    # sentry/db/__init__.py
    value = 1 / 3
    value = 1 // 3


def example10():
    # sentry/db/models/fields/gzippeddict.py
    class GzippedDictField(object):
        __metaclass__ = ABCMeta
