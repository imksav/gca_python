import unittest
from pnz import check


class TestPNZ(unittest.TestCase):
    def test_positive(self):
        self.assertGreater(pnz(5), "+ve")
