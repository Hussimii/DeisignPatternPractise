#!/ usr/bin/python3
# -*- coding: utf-8 -*-
# filename:test_demo.py

try:
    import unittest2 as unittest
except ImportError:
    import unittest


import module_demo
import doctest
from mydict import MyDict


def load_test(loader, tests, ignore):
    """Run doctests from module_demo.py"""
    tests.addTests(doctest.DocTestSuite(module_demo))
    return tests


add = module_demo.add


class test_Add_Args(unittest.TestCase):
    """
    test arguments send to add()
    """

    def test_inputs(self):
        self.assertEqual(add(12), 16)
        self.assertEqual(add(12.0), 16)
        self.assertEqual(add('12.0'), 16)
        self.assertEqual(add('-12.0'), -8)
        self.assertEqual(add(-12.0), -8)


class TestDict(unittest.TestCase):

    def testInit(self):
        myDictTest = MyDict(a=1, b='test')
        self.assertEqual(myDictTest.a, 1)
        self.assertEqual(myDictTest.b, 'test')
        self.assertIsInstance(myDictTest, dict)

    def testKey(self):
        myDictTest = MyDict()
        myDictTest['key'] = 'value'
        self.assertEqual(myDictTest.key, 'value')

    def testValue(self):
        myDictTest = MyDict()
        myDictTest.key = 'value'
        self.assertTrue('key' in myDictTest)
        self.assertEqual(myDictTest['key'], 'value')

    def testKeyError(self):
        myDictTest = MyDict()
        with self.assertRaises(KeyError):
            value = myDictTest['empty']

    def testAttrError(self):
        myDictTest = MyDict()
        with self.assertRaises(AttributeError):
            value = myDictTest.empty


if __name__ == '__main__':
    unittest.main()
