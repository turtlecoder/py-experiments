import unittest
import turtlecoder.experimental.arithmetic as arithmetic


class AdderUnitTests(unittest.TestCase):

    def test_adder(self):
        self.assertEqual(2, arithmetic.add(1, 1))
