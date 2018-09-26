import unittest
import turtlecoder.experimental.arithmetic as arithmetic


class ArithmeticUnitTests(unittest.TestCase):

    def test_adder(self):
        self.assertEqual(2, arithmetic.add(1, 1))

    def test_multiply(self):
        self.assertEqual(4, arithmetic.multiply(2, 2))

    def test_power(self):
        self.assertEqual(4, arithmetic.power(2, 2))

    def test_divide(self):
        self.assertAlmostEqual(2.00000, arithmetic.divide(4, 2), "Some epsilon error")
