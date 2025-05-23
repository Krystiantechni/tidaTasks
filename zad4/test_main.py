import unittest
from main import pies

class xxpiesxx(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(pies(0), [])
        self.assertEqual(pies(-1), [])
        self.assertEqual(pies(27), [])
    
    def test_ein_letter(self):
        self.assertEqual(pies(1), ['a'])
    
    def test_zwie_letters(self):
        exp = ['ab', 'ba']
        self.assertEqual(pies(2), exp)
    
    def test_drei_letters(self):
        exp = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual(pies(3), exp)
    
    def test_vier_letters(self):
        res = pies(4)
        self.assertEqual(len(res), 24)
        self.assertEqual(res[0], 'abcd')
        self.assertEqual(res[-1], 'dcba')

if __name__ == '__main__':
    unittest.main()