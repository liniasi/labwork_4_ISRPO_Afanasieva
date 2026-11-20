import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(10,0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10,10)
        self.assertEqual(res, 100)

    def test_rect_area(self):
        res = area(3,5)
        self.assertEqual(res, 15)

    def test_perimeter(self):
        res = perimeter(3,5)
        self.assertEqual(res, 16)

    def test_float_area(self):
        res = area(0.1,3)
        self.assertAlmostEqual(res, 0.3)

if __name__ == "__main__":
    unittest.main()