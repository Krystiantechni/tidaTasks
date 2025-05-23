import unittest
from main import kot

class xxkotxx(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(kot([]), [])
    
    def test_single(self):
        self.assertEqual(kot([5]), [5])
        self.assertEqual(kot([-5]), [-5])
    
    def test_example_from_adrian(self):
        num = [2, -4, 6, 8, -10, 100, -6, 5]
        exp = [6, 8, -10, 100]
        self.assertEqual(kot(num), exp)
    
    def test_positive(self):
        num = [1, 2, 3, 4, 5]
        self.assertEqual(kot(num), num)
    
    def test_negative(self):
        num = [-5, -4, -3, -2, -1]
        self.assertEqual(kot(num), [-1])
    
    def test_equal_sum_subsequences(self):
        num = [1, 2, 3, -6, 1, 2, 3]
        self.assertEqual(kot(num), [1, 2, 3])
    
    def test_alternating_signs(self):
        num = [1, -1, 1, -1, 1]
        self.assertEqual(kot(num), [1, -1, 1, -1, 1])
    
    def test_zero_in_sequence(self):
        num = [0, 1, 2, 0, 3, 4, 0]
        self.assertEqual(kot(num), [0, 1, 2, 0, 3, 4, 0])

if __name__ == '__main__':
    unittest.main()