import unittest

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Divide by zero!")
    return a / b


class TestCalculator(unittest.TestCase):
    def test_add(self): self.assertEqual(add(6, 2), 8)
    def test_sub(self): self.assertEqual(subtract(17, 9), 8)
    def test_mul(self): self.assertEqual(multiply(4, 3), 12)
    def test_div(self): 
        self.assertEqual(divide(12, 3), 4)
    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            divide(7, 0)

if __name__ == '__main__':
    unittest.main()
