import unittest
from main import kurczak

class xxkurczakxx(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(kurczak([]), [])
    
    def test_single(self):
        self.assertEqual(kurczak([5]), [5])
    
    def test_example_from_adrian(self):
        num = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        exp = [10, 22, 33, 50, 60, 80]
        self.assertEqual(kurczak(num), exp)
    
    def test_increasing(self):
        num = [1, 2, 3, 4, 5]
        self.assertEqual(kurczak(num), num)
    
    def test_decreasing(self):
        num = [5, 4, 3, 2, 1]
        self.assertEqual(kurczak(num), [1])
    
    def test_duplicate(self):
        num = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(kurczak(num), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()