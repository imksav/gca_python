import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 6), 8)

    def test_negative(self):
        self.assertNotEqual(add(2, 3), 7)

    def test3(self):
        self.assertEqual(add(-5, -9), -14)


if __name__ == '__main__':
    unittest.main()
