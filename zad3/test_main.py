import unittest
from main import chomik

class xxchomikxx(unittest.TestCase):
    def test_negativo_y_cero(self):
        self.assertEqual(chomik(-1), [])
        self.assertEqual(chomik(0), [])
    
    def test_uno(self):
        self.assertEqual(chomik(1), [[1]])
    
    def test_dos(self):
        exp = [[1, 1], [2]]
        self.assertEqual(chomik(2), exp)
    
    def test_tres(self):
        exp = [[1, 1, 1], [1, 2], [3]]
        self.assertEqual(chomik(3), exp)
    
    def test_quatro(self):
        exp = [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
        self.assertEqual(chomik(4), exp)
    
    def test_cinco(self):
        exp = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]]
        self.assertEqual(chomik(5), exp)

if __name__ == '__main__':
    unittest.main()