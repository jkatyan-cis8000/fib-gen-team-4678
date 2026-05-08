import unittest
from fibonacci import generate_fibonacci


class TestGenerateFibonacci(unittest.TestCase):
    
    def test_negative_limit(self):
        self.assertEqual(generate_fibonacci(-1), [])
        self.assertEqual(generate_fibonacci(-10), [])
    
    def test_limit_zero(self):
        self.assertEqual(generate_fibonacci(0), [0])
    
    def test_limit_one(self):
        self.assertEqual(generate_fibonacci(1), [0, 1, 1])
    
    def test_basic_cases(self):
        self.assertEqual(generate_fibonacci(2), [0, 1, 1, 2])
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8])
    
    def test_larger_values(self):
        result = generate_fibonacci(100)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(result, expected)
        
        result = generate_fibonacci(1000)
        self.assertEqual(result[-1], 987)
        self.assertLess(result[-2], result[-1])


if __name__ == '__main__':
    unittest.main()
