import unittest
from sub import sub

# python -m unittest tests.test_sub


class TestSub(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(sub(6, 9), -3)

    def test_negative(self):
        self.assertNotEqual(sub(6, 9), 3)

    def test3(self):
        self.assertEqual(sub(-6, 5), -11)

    def test_exception(self):
        self.assertRaises(TypeError, sub, 3)
