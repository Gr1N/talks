# -*- coding: utf-8 -*-

import time
import sys
import unittest

from rainbowrunners.runner import NyanCatRunner

import meetuptopy3k


class DevNull(object):
    def write(self, data):
        pass


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old_stderr = sys.stdout
        sys.stdout = DevNull()

    @classmethod
    def tearDownClass(cls):
        sys.stdout = cls.old_stderr


def test_generator(method):
    def test(self):
        time.sleep(0.1)
        method()
    return test


for i in range(10):
    test_idx = i + 1
    test_method = 'example{0}'.format(test_idx)
    test_name = 'test_{0}'.format(test_method)

    setattr(Tests, test_name, test_generator(getattr(meetuptopy3k, test_method)))


suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
NyanCatRunner().run(suite)
