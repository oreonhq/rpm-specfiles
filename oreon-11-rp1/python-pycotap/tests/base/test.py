#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

from pycotap import TAPTestRunner
from pycotap import LogMode


class SimpleTest(unittest.TestCase):
    @classmethod
    def function_name(cls):
        sys.stdout = sys.__stdout__
        return sys._getframe().f_back.f_code.co_name

    @classmethod
    def setUpClass(cls):
        print(cls.function_name())

    def setUp(self):
        print(SimpleTest.function_name())

    def main(self):
        print(SimpleTest.function_name())

    def test_foo(self):
        print(SimpleTest.function_name())


def main():
    loader = unittest.TestLoader()
    runner = TAPTestRunner(test_output_log=LogMode.LogToError)
    unittest.main(testRunner=runner, testLoader=loader)

if __name__ == '__main__':
    main()
